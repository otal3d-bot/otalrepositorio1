# Suporte V3 — alojamentos facetados, uma vara a 25°

A V3 altera a geometria dos STL, além do perfil de impressão. Mantém a base circular de 140 mm, um porta-varas a 25° da vertical, um alojamento de guarda-sol, buchas intercambiáveis e duas borboletas com parafusos/porcas M6 metálicos.

## Mudanças em relação à V2 e à referência fotográfica

- Corpos externos octogonais, colar inferior escalonado e nervuras triangulares; interior dos alojamentos continua circular.
- Módulos independentes aparafusados à base, sem a calha aberta superior nem as ligações entre tubos da referência.
- Chanfro superior no disco, conservando o envelope de 140 × 140 mm e os centros dos furos.
- Reforços dos apertos com raiz dentro da parede e rampa mais longa, removendo faces inferiores suspensas.
- Dreno da peça inclinada alinhado à cavidade e aberto até ela, eliminando o teto cego.
- Transição contínua do encaixe hexagonal à abertura circular, sem degrau interno suspenso.
- Tetos dos furos em gota e das janelas das buchas a 60° da horizontal, com margem em relação ao limite usual de 45°.
- Recorte de folga no pé do porta-varas para acomodar o novo colar vertical.

O objetivo é uma linguagem visual facetada diferente da referência. Não representa parecer sobre patentes ou liberdade comercial.

## Impressão

Abrir `Jetski_A1_PETG_V3_FACETADO_25GRAUS.3mf` como projeto no Bambu Studio. Perfil A1, bico de 0,4 mm, PETG, camada de 0,24 mm, **3 paredes e 15% gyroid**, seis camadas superiores/inferiores, brim de 6 mm e suportes desligados. Temperaturas e velocidades seguem o perfil V2. Estimativa de fatiamento: **17 h 23 min e 332,95 g**, em uma mesa; não é tempo/peso medido de impressão.

Preservar a orientação dos STL: base, módulos e borboletas com suas superfícies planas na mesa; buchas com flange na mesa; sapatas com cavidade para cima. O tubo inclinado já é modelado a 25° e se imprime com o pé horizontal. Não usar a orientação da imagem de montagem para orientar buchas na impressão.

São nove instâncias impressas: base, guarda-sol, porta-varas, bucha de 25 mm, bucha de 28 mm, duas borboletas e duas sapatas. Os STL de buchas de 22 e 32 mm são alternativas, não peças adicionais da mesma mesa.

## Validação digital

- Nove arquivos STL fechados, sem arestas não manifold.
- Análise dos triângulos: nenhuma face inferior acima de 45° da vertical fora do plano da mesa, nas orientações fornecidas. Arquivo: `validacao-malhas.json`.
- Montagem: sem interseção volumétrica entre módulos; contato plano intencional em z=10 mm entre módulo vertical e base; pé dentro do círculo da base. Arquivo: `validacao-montagem.json`.
- Bambu Studio 02.08.02.61: exportação do 3MF com nove objetos, G-code válido e nenhuma trajetória de suporte. Arquivo: `validacao-3mf.json`.
- Diagnóstico adicional com suportes automáticos habilitados e limiar de 45°: nenhuma trajetória de suporte em ambas as mesas do diagnóstico. O arranjo com suportes habilitados reserva mais espaço e separa a base; o projeto final com suportes desligados permanece em uma mesa. Arquivo: `validacao-suportes-auto.json`.

A checagem de faces não simula adesão, resfriamento, empenamento ou qualidade de pontes. A impressão física ainda deve confirmar acabamento e encaixes. A geração das miniaturas internas do 3MF tem limitação gráfica neste ambiente; `montagem-prototipo.png` foi renderizada separadamente da geometria real.

## Regenerar

Ferramentas: OpenSCAD 2021.01, Blender 4.3.2, Python 3 e Bambu Studio 02.08.02.61. Na pasta `projeto-jetski/v3`:

```bash
python3 gerar_stl.py
python3 validar_malhas.py
blender -b --python renderizar.py
JETSKI_TOOLS=/workspace/onboarding python3 fatiar.py
```

`JETSKI_TOOLS` deve apontar para a instalação preparada do Bambu Studio, contendo `squashfs-root`, `apt/root` com Xvfb/bibliotecas e diretórios graváveis de configuração/cache. O fatiador inicia e encerra Xvfb em :197; não executar cópias simultâneas. Estes comandos regeneram os artefatos desta versão. Para experimentar sem alterá-los, usar uma cópia da pasta e definir `JETSKI_TOOLS`.

## Ferragens, montagem e limites

Usar a lista `FERRAGENS.csv` e a sequência de montagem da [V2](../v2/LEIA-ME.md#montagem-das-peças-entre-si), mantendo as peças da V3 juntas. Não misturar módulos de revisões diferentes sem conferir as folgas. A sapata continua removível e não cativa. Usar porca M6 normal nos reforços e parafuso sextavado M6 × 45 mm nas borboletas.

**Protótipo sem validação física de resistência, vedação ou compatibilidade OEM.** A redução de paredes e preenchimento foi solicitada para este protótipo; não certifica uma carga admissível. Permanecem pendentes os ensaios físicos descritos na V2, incluindo montagem no casco, aperto, retenção, vento, vibração e exposição ao ambiente marinho.
