# Suporte modular para varas e guarda-sol — protótipo V1

Projeto próprio criado para Bambu Lab A1, bico 0,4 mm e PETG. O conjunto tem dois porta-varas verticais e um alojamento central removível para guarda-sol. O projeto usa o posicionamento dos três furos de uma referência CAD pública beta. **Não está validado para instalação, carga, estanqueidade, compatibilidade universal ou venda.**

## Arquivos e peças

- `Jetski_A1_PETG_PROTOTIPO.3mf`: projeto nativo gerado e fatiado no Bambu Studio, com perfis de máquina, material e processo, peças orientadas e G-code incorporado. Contém 1 base, 2 porta-varas, 1 módulo de guarda-sol e 1 bucha nominal de 28 mm.
- `stl/`: sete geometrias individuais. Imprimir o porta-varas duas vezes. As buchas de 22, 25 e 32 mm são alternativas; não precisam ser impressas junto com a bucha de 28 mm.
- `conjunto.scad`: CAD paramétrico editável em OpenSCAD. Alterar `peca` para `base`, `porta_vara`, `guarda_sol`, `bucha` ou `montagem`. `diametro_bucha` define a medida nominal da bucha.
- `montagem-prototipo.png` e `.blend`: visualização da montagem. As cores ajudam a distinguir peças; o projeto de impressão usa um único PETG e não precisa de AMS. Ferragens não estão representadas na imagem.
- `perfis/`: perfis completos utilizados no fatiamento, derivados dos perfis oficiais do Bambu Studio 02.08.02.61.
- `validacao-malhas.json` e `validacao-3mf.json`: resultados das verificações geométricas e do arquivo final. `estimativas.json`: tempo e consumo calculados pelo fatiador.

## Dimensões e interface candidata

Base circular de 140 mm com abas laterais; envelope da base 214 × 140 × 38 mm. A placa tem 10 mm e um espigão sextavado de 44 mm entre faces para o módulo central. O encaixe feminino foi desenhado com 44,6 mm entre faces, correspondendo a 0,3 mm por lado, antes das variações reais de impressão. Isso é uma tolerância inicial, não uma garantia de ajuste.

Os três furos da interface candidata têm 7 mm e centros (58,10935; −1,01371), (−16,06119; −55,94250) e (−14,63087; 56,77056), relativos ao centro da base. Distâncias entre centros: 92,295, 112,722 e 92,899 mm. Estes valores foram extraídos de um STL sem unidade explícita, interpretado em milímetros. O suporte original do anúncio não foi medido.

Porta-varas: altura 150 mm, abertura de 36 mm, parede principal de 5 mm, raiz alargada, flange de 8 mm e drenagem inferior de 8 mm. Dois furos de fixação de 6,6 mm, separados por 64 mm. Furo passante horizontal para um pino metálico opcional de apoio da vara.

Guarda-sol: altura 150 mm, corpo de 56 mm de diâmetro externo e abertura superior de 36 mm. Raiz alargada de 68 mm. Buchas com diâmetro externo de 35,5 mm e aberturas nominais de 22, 25, 28 ou 32 mm, acrescidas de 0,5 mm de folga diametral. Uma flange impede que a bucha desça pelo tubo. Cortes superiores permitem aperto por abraçadeira metálica. A eficácia desse aperto ainda precisa ser ensaiada.

## Ferragens para montar o protótipo fora do jet ski

Preferir aço inox A4/316. Medidas nominais abaixo calculadas para as peças deste desenho, com arruelas planas M6 de aproximadamente 12 mm de diâmetro externo e 1,6 mm de espessura. Comprimentos são medidos sob a cabeça. Não substituir pelas arruelas largas de 18 mm sem verificar interferência com os reforços.

| Quantidade | Item | Função |
|---:|---|---|
| 4 | Parafuso M6 × 30 mm, cabeça cilíndrica Allen | Fixar os dois porta-varas à base |
| 1 | Parafuso M6 × 80 mm, cabeça cilíndrica Allen | Retenção transversal do módulo central |
| 2, opcionais | Parafuso M6 × 60 mm, cabeça cilíndrica Allen | Pinos transversais internos dos porta-varas |
| 5; ou 7 com os pinos | Porca M6 autotravante | União dos módulos e pinos |
| 10; ou 14 com os pinos | Arruela plana M6, diâmetro externo 12 mm | Duas por união |
| 1 | Abraçadeira inox ajustável Ø 50–70 mm, fita de até 12 mm | Apertar a região superior do alojamento do guarda-sol |

Os pinos opcionais podem precisar de proteção macia para evitar desgaste nos cabos das varas. Não apertar o PETG usando torques de união metal–metal; aperto, retenção e deformação devem ser verificados em ensaio.

**Os três parafusos de fixação ao Sea-Doo permanecem sem especificação confirmada.** Furos de 7 mm não provam que a rosca do casco é M6. Comprimento útil, cabeça, passo, profundidade disponível, apoio e interferência com a tampa original ainda precisam ser identificados. As porcas das abas também exigem espaço livre inferior; esse espaço não foi confirmado no veículo. Não furar nem modificar o casco a partir deste protótipo.

## Impressão

O 3MF preserva as orientações de projeto: base com face inferior na mesa, tubos verticais apoiados nas respectivas raízes/flanges e bucha apoiada pela flange. Os furos horizontais usam formato de gota com teto a 45°. A transição interna do módulo central é inclinada. Não há estruturas de suporte no fatiamento; brim é uma borda de adesão removível, não um suporte.

| Configuração | Valor |
|---|---|
| Impressora / bico | Bambu Lab A1 / 0,4 mm |
| Mesa | Textured PEI Plate |
| Material | Generic PETG @BBL A1, perfil oficial |
| Camada / primeira camada | 0,24 / 0,24 mm |
| Paredes | 6 |
| Camadas superiores / inferiores | 6 / 6 |
| Preenchimento | Gyroid 30% |
| Suportes | Desligados |
| Brim exterior | 6 mm, afastamento 0,15 mm |
| Parede externa / interna | 45 / 70 mm/s |
| Vazão volumétrica máxima | 8 mm³/s |
| Bico / mesa | 255 °C / 80 °C, conforme perfil genérico oficial |
| Aceleração geral / externa | 2.000 / 1.000 mm/s² |

A camada de 0,24 mm reduz o número de camadas em relação a 0,20 mm. O projeto prioriza paredes e reforços em vez de preenchimento integral da base. Não foi demonstrado um ótimo global de tempo ou resistência. A orientação vertical evita suportes, mas mantém a anisotropia de resistência entre camadas do processo FDM.

O conjunto principal foi acomodado em **uma mesa** pelo Bambu Studio. Estimativa final: **30 h 27 min e 641 g de PETG**, incluindo brim e procedimentos da máquina. As três buchas alternativas ficam fora dessa estimativa. O fatiador terminou com sucesso e sem avisos nas peças; o 3MF foi reaberto pelo mesmo programa e os cinco objetos foram reconhecidos como malhas fechadas. O exportador não conseguiu gerar miniaturas por uma limitação gráfica do ambiente; a imagem de montagem foi renderizada separadamente no Blender.

Antes de imprimir, abra o 3MF como **projeto** no Bambu Studio e confira máquina, bico e mesa. Se o PETG do fabricante pedir temperaturas diferentes, ajuste o material, calibre vazão/adesão e refatie. O G-code incluído foi gerado para o perfil descrito; não usar em outra impressora ou bico. PETG úmido e fluxo não calibrado prejudicam o encaixe e a união entre camadas. As estimativas são do fatiador, não de impressão física.

## Sequência de montagem do conjunto

1. Retirar brim, rebarbas e fios. Inspecionar os furos e as uniões entre camadas. Não forçar o encaixe sextavado.
2. Colocar o módulo central sobre o espigão da base, alinhar o furo e instalar o M6 × 80 mm com duas arruelas e porca.
3. Fixar cada porta-varas à aba correspondente com dois M6 × 30 mm, arruelas e porcas. Há necessidade de acesso inferior às porcas.
4. Instalar os dois pinos M6 × 60 mm apenas se o tipo de cabo da vara exigir esse apoio.
5. Escolher uma única bucha. Inserir com o corpo no tubo e a flange apoiada na boca. A bucha é impressa pela flange e fica invertida na montagem.
6. Posicionar a abraçadeira no canal superior e testar o aperto da haste, sem esmagar as peças.

Esta sequência monta somente as peças entre si. Não é uma instrução validada de instalação no jet ski. Alguns parafusos da interface ficam próximos aos módulos laterais; o acesso precisa ser conferido com os módulos removidos.

## Limites e próximos testes

O modelo público que orientou a interface é [Sea-doo Pylon Cover Flag / Umbrella Holder (Beta), por AHAC EL](https://www.printables.com/model/1133098-sea-doo-pylon-cover-flag-umbrella-holder-beta). Seu autor informa que precisa de ajustes; não declara compatibilidade com todos os Sea-Doo. A geometria dos módulos deste protótipo foi desenhada de forma independente. Não foi feita análise das reivindicações da patente citada pelo usuário; diferença visual não comprova liberdade comercial de exploração.

A base não reproduz uma tampa OEM estanque, travas inferiores, juntas ou ressaltos de apoio confirmados. Não deve substituir uma tampa de vedação sem projeto e teste específicos. O envelope, as porcas inferiores e o acesso às fixações precisam ser verificados em uma tampa/veículo identificado.

Não foi realizado ensaio de encaixe, carga, vento, fadiga, vibração, exposição solar, água salgada ou estanqueidade. Não há carga admissível ou tamanho máximo de guarda-sol certificado. O guarda-sol aberto foi considerado somente com o veículo parado; isso não valida segurança sob vento. Não anunciar como universal, resistente em determinado grau, apto a navegação ou pronto para venda com base apenas no fatiamento. Para venda, é necessário testar o conjunto em referência física identificada e avaliar a fixação e as cargas do uso proposto.
