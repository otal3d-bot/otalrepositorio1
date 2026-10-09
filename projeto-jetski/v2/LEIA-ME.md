# Suporte para uma vara e um guarda-sol — protótipo V2

Esta revisão substitui o desenho V1: **base somente circular de 140 mm, um único porta-varas a 25° da vertical, um alojamento vertical para guarda-sol e duas borboletas de aperto manual**. As fixações dos módulos ficam dentro do disco; não há abas laterais na base. O tubo inclinado se projeta para fora do disco na parte superior, como consequência da angulação; o contorno de apoio permanece circular.

## Arquivos e quantidades

`Jetski_A1_PETG_V2_CIRCULAR_25GRAUS.3mf` é um projeto nativo do Bambu Studio para A1, bico 0,4 mm e PETG. Abrir como **projeto**, não somente como geometria. O fatiamento inclui nove peças:

| Quantidade | Peça |
|---:|---|
| 1 | Base circular |
| 1 | Porta-varas inclinado a 25° |
| 1 | Suporte vertical para guarda-sol |
| 1 | Bucha nominal de 25 mm para a vara |
| 1 | Bucha nominal de 28 mm para o guarda-sol |
| 2 | Manípulo borboleta para parafuso M6 metálico |
| 2 | Sapata de pressão removível |

Os diâmetros de 25 e 28 mm são escolhas iniciais, não medidas da referência. Buchas alternativas de 22 e 32 mm estão em `stl/`. As quatro opções usam o mesmo diâmetro externo de 35,5 mm e folga interna inicial de 0,5 mm sobre o nominal. Usar somente uma bucha por alojamento. Sem bucha, a abertura nominal dos tubos é de 36 mm.

`conjunto.scad` contém o CAD paramétrico. `angulo_vara=25` controla a angulação. Alterar esse valor exige regenerar as peças, conferir a montagem e refatiar; o ângulo não é ajustável durante o uso. `montagem-prototipo.png` e `.blend` mostram a montagem. As cores são ilustrativas; não há necessidade de AMS. Algumas ferragens aparecem na imagem somente para mostrar o funcionamento e não estão no 3MF de impressão.

## Como funciona o aperto com borboleta

A borboleta impressa recebe a **cabeça sextavada de um parafuso M6 × 45 mm metálico**, entre faces de 10 mm. Uma contraporca fina sob a borboleta prende o manípulo ao parafuso. A borboleta gira junto com o parafuso.

Cada alojamento tem um reforço com uma cavidade aberta por cima para uma **porca M6 normal metálica**, entre faces de 10 mm e espessura nominal de 5 mm. Essa porca fica impedida de girar. Ao girar a borboleta, o parafuso avança pela porca e pressiona o cabo. A rosca funcional é metálica; não depende de uma rosca M6 impressa em PETG.

As buchas têm uma janela lateral para passagem da sapata de pressão. Alinhar essa janela com o parafuso. A sapata tem uma cavidade rasa para apoiar a ponta do parafuso e distribuir o contato com a haste. Ela é removível e ainda não tem retenção cativa: pode cair ao soltar completamente o aperto. Para montagem, colocar a haste, posicionar a sapata pela abertura e avançar o parafuso até apoiar, sem esmagar o material. Avaliar retenção, desgaste e força de aperto no protótipo físico.

## Ferragens deste desenho

Preferir aço inox A4/316. Comprimentos dos parafusos medidos sob a cabeça.

| Quantidade | Ferragem | Uso |
|---:|---|---|
| 2 | M6 × 30 mm, cabeça cilíndrica Allen | Fixação do porta-varas à base |
| 1 | M6 × 70 mm, cabeça cilíndrica Allen | Retenção transversal do módulo do guarda-sol |
| 2 | M6 × 45 mm, cabeça sextavada de 10 mm, totalmente roscado | Parafusos acionados pelas borboletas |
| 3 | Porca M6 autotravante | Dois parafusos da base e retenção transversal |
| 2 | Porca M6 normal, AF 10 mm, altura nominal 5 mm | Cavidades dos apertos manuais |
| 2 | Contraporca M6 fina, altura aproximada 3 mm | Fixar cada borboleta à cabeça do seu parafuso |
| 6 | Arruela M6, diâmetro externo 12 mm, espessura aproximada 1,6 mm | Duas por união estrutural |
| 3, a confirmar | Parafusos de fixação OEM | Fixação ao jet ski ainda sem medidas comprovadas |

Não usar parafuso Allen dentro da borboleta: o alojamento foi desenhado para cabeça sextavada. Não usar porca autotravante espessa no alojamento dos apertos: a geometria foi feita para porca normal de 5 mm. Conferir dimensões reais das ferragens antes de comprar um lote.

As duas porcas sob a base exigem espaço inferior. Essa folga não foi confirmada no veículo. O contorno circular de 140 mm não demonstra que a parte inferior, as porcas ou a vedação encaixem no Sea-Doo. Furos de 7 mm não comprovam rosca OEM M6 nem comprimento dos parafusos do casco.

## Impressão e validação digital

Perfil: A1, bico 0,4 mm, mesa PEI texturizada, Generic PETG oficial, camadas de 0,24 mm, seis paredes, gyroid 30%, seis camadas superiores/inferiores, brim externo de 6 mm, suportes desligados. Bico 255 °C, mesa 80 °C e vazão máxima de 8 mm³/s, conforme perfil genérico oficial. Ajustar o material às recomendações do fabricante do filamento e refatiar se necessário.

Todas as peças ficam na orientação de projeto. O porta-varas é impresso com o pé horizontal e o tubo já inclinado a 25°. Os furos horizontais usam teto em gota; a janela da bucha e as transições dos reforços usam teto/rampa inclinados. O brim é uma borda removível de adesão, não uma estrutura de suporte.

O Bambu Studio 02.08.02.61 fatiou o conjunto e reabriu o 3MF com sucesso, reconhecendo as nove peças como malhas fechadas. O G-code foi verificado sem recursos de suporte. A base foi conferida com envelope XY de 140 × 140 mm e todos os vértices dentro do círculo de raio 70 mm. A interseção entre o módulo de guarda-sol e o porta-varas deu volume vazio, assim como a diferença entre o pé do porta-varas e o contorno circular. Esses checks validam geometria e fatiamento, não resistência física ou encaixe OEM.

Estimativa final do fatiador: **24 h 55 min e 507 g de PETG, em uma mesa**, incluindo as duas buchas escolhidas, borboletas, sapatas e brim. Não é tempo de impressão medido. O exportador não gerou miniaturas por uma limitação gráfica do ambiente; a montagem foi renderizada separadamente.

## Montagem das peças entre si

1. Remover brim e rebarbas; conferir as cavidades e os furos. Montar fora do veículo.
2. Encaixar o módulo vertical no espigão sextavado deslocado da base. Alinhar o furo e instalar o M6 × 70 mm, duas arruelas e porca autotravante.
3. Apoiar o único porta-varas no disco e fixar com dois M6 × 30 mm, quatro arruelas e duas porcas autotravantes. As coordenadas dos furos são (12; 50) e (16; 6), em milímetros relativos ao centro do disco.
4. Introduzir as porcas normais M6 nos dois reforços de aperto, pelas aberturas superiores. Usar os parafusos apenas após a porca estar assentada.
5. Introduzir cada M6 × 45 mm pela cavidade sextavada da borboleta e prender com contraporca fina sob a peça. A cabeça deve permanecer apoiada na cavidade.
6. Inserir a bucha adequada pela boca do tubo, com flange apoiada e janela voltada para o parafuso. No tubo inclinado, a bucha acompanha a inclinação.
7. Instalar haste e sapata; rosquear a borboleta com cuidado até obter contato. Não usar torques de montagem metal–metal no PETG.

Esta sequência não é uma instrução de instalação validada no casco. O acesso aos três parafusos OEM pode exigir remover os módulos. Não furar nem modificar o jet ski a partir deste protótipo.

## Limites

A posição dos três furos OEM ainda vem do [CAD público beta de AHAC EL](https://www.printables.com/model/1133098-sea-doo-pylon-cover-flag-umbrella-holder-beta), cujo autor diz que precisa de ajustes. STL sem unidade explícita, interpretado em milímetros. Diâmetro externo candidato de 140 mm; furos de passagem de 7 mm; distâncias entre centros 92,295 / 112,722 / 92,899 mm. Não há comprovação de compatibilidade com todos os modelos Sea-Doo.

A V2 conserva as funções solicitadas — alojar uma vara inclinada, alojar um guarda-sol e permitir aperto manual — com uma solução própria. Não foi feito levantamento completo das peças ocultas do anúncio nem análise das reivindicações da patente. Diferença visual não garante liberdade comercial de exploração.

**Protótipo sem validação física para venda ou uso embarcado.** Faltam ensaios de montagem, aperto, retenção, carga, fadiga, vento, vibração, exposição solar, água salgada e vedação. A peça não reproduz uma tampa OEM estanque. Não há carga admissível ou tamanho de guarda-sol certificado. Guarda-sol aberto foi considerado somente com o veículo parado; isso não valida segurança em vento. A angulação do porta-varas também não certifica retenção da vara em movimento.
