# Revisão facetada do `completo.3mf` — duas peças

Esta revisão parte do 3MF enviado pelo usuário: `Seadoo Double Rod Holder v2.STL` e `Rod Holder extension v2.STL`. Continua com **exatamente duas peças de montagem**: o corpo com os dois tubos e a extensão curva. As revisões V1/V2/V3 existentes no repositório são trabalhos anteriores; não definem esta geometria.

## Alterações

- Faces externas planas nos dois tubos e no pedestal; alojamentos internos circulares preservados.
- Rampas facetadas integradas sob os tubos e nas duas ligações entre eles, substituindo regiões que exigiam apoio.
- Curva da extensão reduzida de aproximadamente 67,44° para **45°**, conforme solicitado. Exterior da extensão facetado e canal interno nominal de 41,275 mm.
- Zona de inserção da extensão e face inferior do batente preservadas a partir da malha original. A zona protegida termina em Y = −5,03302 mm nas coordenadas do arquivo original; a nova curva começa em Y = 1,18 mm. O pequeno alívio interno da saída começa em Y = −4,5 mm e fica fora da inserção.
- Abertura do berço com término em arco pontudo, para que o fechamento cresça das paredes laterais.
- Ponta aberta com face plana de apoio e bordas contínuas: os pequenos entalhes laterais foram retirados porque criavam abas que começavam suspensas. A face de apoio modifica o contorno da ponta e mantém a altura de impressão em **254 mm** na A1, sem cortar o encaixe.

A base original tem aproximadamente **134,985 mm** de diâmetro. Seus furos foram conservados; não foi substituída pela base de 140 mm das revisões anteriores. A estética nova não constitui análise de patentes ou autorização de exploração comercial.

## Arquivos para imprimir

- `completo_duas_pecas_facetado.3mf`: abrir como **projeto** no Bambu Studio, mantendo a orientação e o perfil salvos.
- `STL_duas_pecas.zip`: contém somente `corpo_revisado.stl` e `extensao_revisada.stl`, nas respectivas orientações de impressão.
- `montagem_facetada.png` e `montagem_costas.png`: vistas da montagem. A posição de uso da extensão na imagem é diferente de sua posição na mesa.

Perfil solicitado: Bambu A1, bico 0,4 mm, PETG, camada de 0,20 mm, **3 paredes e 15% gyroid**, cinco camadas superiores e três inferiores. As alturas de camada e quantidades de camadas superiores/inferiores acompanham o arquivo original; o original usava 2 paredes e 8% gyroid. Há brim de 6 mm para adesão, removível após a impressão. O brim não é uma peça de montagem nem um suporte de overhang.

**Preservar a orientação da extensão no projeto.** Virá-la para a posição de uso ou acionar orientação automática pode voltar a criar regiões que precisem de suporte. Altura máxima da extensão na posição fornecida: 254 mm, dentro dos 256 mm nominais da A1.

## Verificação

`validacao-malhas.json` registra fechamento, componentes conectados e dimensões. Cada STL possui uma única componente conectada e nenhuma aresta não manifold. A análise geométrica registra pequenos resíduos na transição interna da extensão (cerca de 0,19 mm²); isso não é tratado como uma prova isolada de impressão sem suportes. No diagnóstico com os parâmetros de detecção do original (árvore automática, 30°), nenhuma trajetória de suporte foi gerada. Um teste adicional com suporte normal a 45° ainda sugere apoios na extensão; portanto não se afirma que ela dispense apoio em qualquer perfil ou orientação. Os resultados ficam em `validacao-suportes-auto.json`, `validacao-extra-45.json` e `validacao-3mf.json`.

O projeto final tem dois objetos, em uma mesa, sem trajetórias de suporte. Estimativa: **36 h 09 min 30 s e 619,16 g de PETG**. As estimativas finais do fatiador estão em `estimativas.json`. Tempos e consumo são estimativas digitais, não medições de impressão. A imagem de montagem é renderizada da geometria dos STL entregues. Miniaturas internas do 3MF podem não estar disponíveis devido à limitação gráfica do ambiente de exportação.

**Protótipo com validação digital.** Impressão física, encaixe no veículo, retenção, resistência e vedação ainda precisam de ensaio. Preservar dimensões do arquivo original não comprova que ele seja compatível com um veículo específico.

## Regeneração

Ferramentas utilizadas: OpenSCAD 2021.01, Python 3 com NumPy, Blender 4.3.2 e Bambu Studio 02.08.02.61. As malhas em `fontes/` são referências de construção; os únicos STL de impressão ficam em `stl/`.

```bash
cd projeto-jetski/duas-pecas
python3 fontes/gerar.py
python3 validar_malhas.py stl/corpo_revisado.stl stl/extensao_revisada.stl
JETSKI_TOOLS=/workspace/onboarding python3 fatiar.py
```

O fatiador utiliza a instalação preparada em `JETSKI_TOOLS` (`squashfs-root`, `apt/root` com Xvfb e bibliotecas). Para repetir o diagnóstico de suportes, usar `JETSKI_AUTO_SUPPORT_TEST=1` junto do mesmo comando. Isso produz um projeto de teste; execute novamente sem essa variável para gerar o projeto final com suportes desligados. O script inicia e encerra seu próprio Xvfb; não execute duas cópias simultâneas.
