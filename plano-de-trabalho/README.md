# Plano de Trabalho — Robô Bio

> Versão revisada após feedback do orientador (inclui hipótese científica, formulação da função de custo, análise de desempenho computacional e atualização de referências). Documento-fonte original: [`Plano_de_trabalho_Bio_Felipe_das_Neves.pdf`](./Plano_de_trabalho_Bio_Felipe_das_Neves.pdf).

**Universidade de Brasília — Decanato de Pesquisa e Pós-Graduação**
**Programa de Iniciação Científica – ProIC/UnB**

---

## DADOS GERAIS DA(O) ORIENTADORA(O)

ÁREA DO CONHECIMENTO: (X) EXATAS ( ) HUMANAS ( ) VIDA

- **Nome do orientador:** Renato Coral Sampaio
- **Titulação do orientador:** (X) Doutor ( ) Recém-Doutor (obtenção do doutorado a partir do início de 2015) ( ) Mestre
- **Departamento principal:** FCTE
- **Área específica do projeto:** Sistemas Embarcados

---

## RESUMO DO PROJETO DE PESQUISA

### Título do Projeto de Pesquisa

Robô Bio: Desenvolvimento de um Sistema de Navegação Autônoma Baseado em Visão Computacional e Controle PID Otimizado por Algoritmos Bioinspirados

### 1) Problema e Objetivos

A crescente adoção de robôs móveis autônomos em aplicações industriais, agrícolas, logísticas e de inspeção tem impulsionado o desenvolvimento de sistemas de navegação cada vez mais robustos, eficientes e adaptáveis. A capacidade de operar de forma autônoma em ambientes dinâmicos representa um dos principais desafios da robótica moderna, exigindo a integração eficiente entre percepção, tomada de decisão e controle. Nesse contexto, problemas relacionados à manutenção da trajetória, estabilidade dinâmica e adaptação a diferentes condições ambientais continuam sendo temas de interesse científico e tecnológico (AMEEN; VOKHIDOV, 2024).

Os robôs seguidores de linha constituem uma plataforma experimental amplamente empregada para validação de técnicas de controle, navegação e inteligência computacional. Tradicionalmente, esses sistemas utilizam sensores de refletância associados a controladores PID para correção da trajetória. Embora essa abordagem apresente baixo custo computacional e simplicidade de implementação, estudos demonstram que seu desempenho tende a se degradar em situações envolvendo altas velocidades, curvas acentuadas, mudanças de iluminação ou imperfeições na pista, tornando necessária a adoção de métodos mais robustos de percepção e controle (OGUTEN; KABAS, 2021).

Paralelamente, avanços recentes em Inteligência Artificial têm possibilitado a aplicação de algoritmos bioinspirados em problemas complexos de otimização. Técnicas como Particle Swarm Optimization (PSO) e Differential Evolution (DE) vêm sendo amplamente utilizadas para ajuste automático de parâmetros de controladores PID, permitindo reduzir o esforço de sintonia manual e melhorar indicadores como erro de rastreamento, estabilidade e tempo de acomodação (KIM; PRAKAPOVICH, 2021). Esses métodos apresentam elevada capacidade de exploração do espaço de busca, sendo particularmente adequados para sistemas não lineares e sujeitos a incertezas.

Outro fator que tem impulsionado o desenvolvimento de sistemas robóticos autônomos é a crescente disponibilidade de plataformas embarcadas de baixo custo e elevado desempenho computacional. Dispositivos como a Raspberry Pi permitem a execução de algoritmos de processamento digital de imagens, visão computacional e controle em tempo real, tornando viável a implementação de sistemas autônomos complexos em plataformas compactas e acessíveis (PASTRANA TRIANA, 2019). Trabalhos recentes demonstram que a utilização de visão computacional embarcada pode superar limitações inerentes aos sensores discretos, fornecendo informações mais ricas sobre o ambiente e aumentando a flexibilidade dos sistemas de navegação (DEWANTORO et al., 2021).

A utilização de câmeras embarcadas associadas a bibliotecas de processamento de imagens, como OpenCV, permite identificar a pista por meio de técnicas de segmentação, filtragem e extração de características em tempo real. Essa abordagem vem sendo aplicada com sucesso em robôs móveis autônomos, proporcionando maior precisão de navegação e capacidade de adaptação a diferentes cenários operacionais (VARGAS TORRES; SANTIAGO-PAZ, 2019; RIHEM; ALJALOUD, 2023).

O projeto Robô Bio surgiu inicialmente como trabalho final da disciplina Fundamentos de Sistemas Embarcados da Universidade de Brasília, utilizando controle PID clássico, sensores de refletância e telemetria baseada em ThingsBoard. Posteriormente, o sistema evoluiu para uma segunda geração com novo chassi modular inspirado no rover open-source ExoMy cuja arquitetura desenvolvido pelo Planetary Robotics Laboratory da European Space Agency (ESA), uma plataforma de baixo custo baseada em Raspberry Pi, ROS e manufatura aditiva destinada à pesquisa e educação em robótica móvel (VOELLMY; EHRHARDT, 2020), proporcionando maior robustez estrutural, modularidade e capacidade de expansão para futuras pesquisas.

A presente proposta visa desenvolver uma nova versão do Robô Bio como uma plataforma modular de pesquisa em robótica móvel autônoma, incorporando visão computacional embarcada e algoritmos bioinspirados para otimização automática dos parâmetros do controlador PID permitindo a validação experimental de algoritmos de visão computacional, controle inteligente e otimização bioinspirada. A combinação dessas tecnologias permitirá investigar estratégias de controle inteligente para navegação autônoma baseada em percepção visual, contribuindo para o avanço das pesquisas em robótica móvel, sistemas embarcados e inteligência artificial aplicada que permitirá, em trabalhos futuros, a substituição dos métodos clássicos de visão computacional por modelos de aprendizado profundo para segmentação de pistas e navegação autônoma.

Diante desse contexto, formula-se a hipótese de que os algoritmos bioinspirados (PSO e DE) são capazes de convergir para conjuntos de parâmetros do controlador PID (Kp, Ki, Kd) que reduzem o erro quadrático médio (RMSE) de rastreamento da trajetória em pelo menos X% em relação à sintonia clássica de Ziegler-Nichols e à sintonia manual, mantendo a estabilidade do sistema em cenários de iluminação variável detectados por visão computacional embarcada, o percentual de referência a ser consolidado após o estabelecimento da linha de base experimental. Espera-se, ainda, que a otimização bioinspirada reduza a dependência de ajuste manual e o esforço de sintonia, e que seja possível identificar uma configuração de hardware e técnicas de otimização que viabilizem a execução conjunta, em tempo real, da visão computacional, do laço de controle e do processo de otimização populacional na plataforma embarcada.

### 3) Metodologia

O projeto será desenvolvido em etapas/atividades técnicas sequenciais ou concomitantes. Cada etapa possui uma meta específica relacionada ao desenvolvimento do Robô Bio e à investigação da aplicação de algoritmos bioinspirados em sistemas de controle para robótica móvel autônoma. Para cada etapa serão estudados conceitos, implementadas metodologias e realizados experimentos que serão posteriormente validados através de testes práticos e análise dos resultados obtidos.

Quando necessário, e dependendo dos resultados experimentais, novas iterações de projeto, implementação e testes serão executadas visando o refinamento contínuo do sistema. Do ponto de vista de gerenciamento, serão aplicados princípios de acompanhamento e avaliação de desempenho para verificar a evolução do projeto e o cumprimento dos objetivos estabelecidos. As informações obtidas durante as fases de validação servirão como realimentação para aprimoramento das etapas subsequentes.

A metodologia técnica aplicada ao projeto será descrita através de etapas analíticas, experimentais e computacionais, que poderão ocorrer de forma sequencial ou paralela, conforme previsto no cronograma de execução.

#### Etapa 1: Revisão Bibliográfica

Levantamento bibliográfico sobre os principais temas relacionados ao projeto, incluindo:

- Robótica móvel autônoma;
- Controle PID;
- Controle adaptativo e controle inteligente;
- Algoritmos bioinspirados para otimização;
- Visão computacional embarcada;
- Sistemas embarcados aplicados à robótica.

Nessa etapa serão identificados os principais trabalhos relacionados ao estado da arte e as metodologias mais adequadas para implementação e validação do sistema proposto.

#### Etapa 2: Desenvolvimento da Plataforma Robótica

Nesta etapa será realizada a modelagem, fabricação e montagem do Robô Bio.

As atividades incluem:

- Refinamento do projeto mecânico;
- Fabricação de componentes por impressão 3D;
- Montagem estrutural do protótipo;
- Integração dos sistemas de alimentação e locomoção;
- Instalação dos motores e sistemas de acionamento.

O principal objetivo desta etapa é obter uma plataforma experimental funcional para realização dos ensaios subsequentes.

#### Etapa 3: Integração dos Sistemas Embarcados

Nesta etapa será realizada a integração dos componentes eletrônicos responsáveis pela aquisição de dados e execução dos algoritmos de controle.

As atividades previstas incluem:

- Configuração da Raspberry Pi;
- Integração da câmera embarcada;
- Configuração dos controladores de motores;
- Implementação dos sistemas de comunicação;
- Desenvolvimento da infraestrutura de telemetria e armazenamento de dados experimentais.

#### Etapa 4: Desenvolvimento do Sistema de Visão Computacional

Nesta etapa será implementado o sistema responsável pela percepção do ambiente.

Serão desenvolvidas rotinas para:

- Aquisição de imagens em tempo real;
- Processamento digital de imagens;
- Filtragem e segmentação da pista;
- Extração da posição relativa da trajetória;
- Geração dos sinais de erro para o controlador.

Os algoritmos serão implementados utilizando OpenCV e executados diretamente na Raspberry Pi.

#### Etapa 5: Implementação do Controle PID

Nesta etapa será desenvolvido o controlador PID responsável pela navegação do robô.

Serão realizadas:

- Modelagem do sistema de controle;
- Implementação dos controladores proporcional, integral e derivativo;
- Ajuste inicial dos parâmetros de controle;
- Ensaios preliminares de navegação.

Nessa etapa será estabelecida a linha de base experimental utilizada para comparação com os métodos bioinspirados.

#### Etapa 6: Implementação dos Algoritmos Bioinspirados

Nesta etapa serão implementados algoritmos bioinspirados para realização da sintonia automática dos parâmetros do controlador PID. Serão inicialmente investigadas as técnicas Particle Swarm Optimization (PSO) e Differential Evolution (DE), devido à sua ampla utilização em problemas de otimização contínua e ajuste de controladores em sistemas robóticos (KIM; PRAKAPOVICH, 2021).

Além dos algoritmos convencionais, serão estudadas estratégias de manutenção artificial de diversidade populacional visando reduzir problemas de convergência prematura e mínimos locais, aumentando a capacidade de exploração do espaço de busca. Os algoritmos serão executados utilizando dados experimentais obtidos pelo robô durante a navegação e terão como objetivo minimizar funções de custo relacionadas ao desempenho do sistema.

As funções objetivo poderão considerar simultaneamente diferentes métricas de desempenho, tais como:

- Erro médio quadrático de seguimento da trajetória;
- Tempo total de percurso;
- Oscilações laterais do robô;
- Tempo de acomodação;
- Consumo computacional.

**Formulação da função de custo (fitness).** A sintonia automática será tratada como um problema de otimização no qual cada indivíduo/partícula representa um vetor de ganhos do controlador, θ = (Kp, Ki, Kd). O desempenho de cada candidato será avaliado por uma função de custo J(θ) calculada a partir dos dados de telemetria coletados durante a navegação. Como as métricas listadas são concorrentes, serão investigadas duas abordagens de modelagem:

- **(a) Soma ponderada (escalarização).** As métricas, previamente normalizadas (ex.: min-max ou z-score, para evitar que grandezas de escalas distintas dominem o resultado), são combinadas em um único escalar:

$$J(\theta) = w_1\,\text{RMSE}_e + w_2\,t_p + w_3\,\sigma_{lat} + w_4\,t_s + w_5\,C_{comp}$$

  em que RMSE_e é o erro quadrático médio de rastreamento, t_p o tempo de percurso, σ_lat as oscilações laterais, t_s o tempo de acomodação e C_comp o custo computacional; os pesos w_i (com Σ w_i = 1) refletem a importância relativa de cada critério. Termos de penalidade serão somados para soluções que violem restrições (ex.: perda da linha/pista ou instabilidade).

- **(b) Otimização multiobjetivo (Fronteira de Pareto).** Como os critérios frequentemente conflitam (reduzir o tempo de percurso, por exemplo, tende a aumentar as oscilações laterais), também será avaliada uma formulação multiobjetivo, gerando um conjunto de soluções não-dominadas (Fronteira de Pareto) por meio de variantes como MOPSO ou NSGA-II / DE multiobjetivo. Essa abordagem permite analisar explicitamente os *trade-offs* entre precisão de rastreamento, velocidade e custo computacional sem fixar pesos a priori.

A escolha final entre escalarização e abordagem de Pareto será definida experimentalmente, comparando a qualidade das soluções, a interpretabilidade dos resultados e o custo computacional de cada estratégia na plataforma embarcada.

Os parâmetros obtidos pelos algoritmos bioinspirados serão posteriormente comparados com métodos clássicos de sintonia PID, permitindo avaliar quantitativamente os ganhos obtidos pela abordagem proposta.

#### Etapa 7: Programa Experimental

Será estabelecido um programa experimental para validação do sistema.

Os experimentos incluirão:

- Navegação em pistas retas;
- Navegação em curvas suaves;
- Navegação em curvas acentuadas;
- Diferentes condições de iluminação;
- Diferentes velocidades de operação.

As métricas analisadas incluirão:

- Erro médio de seguimento da trajetória;
- Tempo de percurso;
- Oscilações laterais;
- Estabilidade do sistema;
- Consumo computacional dos algoritmos.

#### Etapa 8: Análise Comparativa dos Resultados

Nesta etapa serão comparados os resultados obtidos pelos diferentes métodos de sintonia do controlador.

O principal objetivo será comparar:

- PID ajustado manualmente;
- PID ajustado por métodos clássicos;
- PID otimizado por algoritmos bioinspirados.

Os resultados serão avaliados através de métodos estatísticos e análise quantitativa de desempenho.

#### Etapa 9: Análise de Desempenho Computacional e Requisitos de Hardware

A execução simultânea do pipeline de visão computacional (OpenCV), do laço de controle em tempo real e dos algoritmos de otimização populacional (PSO/DE) impõe carga significativa a plataformas embarcadas de baixo custo. Esta etapa investigará, de forma fundamentada em dados, os requisitos computacionais do sistema, em vez de fixar a plataforma de hardware a priori. Serão realizadas:

- Caracterização (*profiling*) do uso de CPU, memória, temperatura e consumo energético durante a navegação;
- Avaliação de estratégias de otimização de desempenho (redução de resolução da imagem / região de interesse, paralelização e *multiprocessing*, execução *offline* da sintonia versus *online*, entre outras);
- Comparação entre diferentes plataformas candidatas (ex.: Raspberry Pi Zero 2W, Raspberry Pi 4/5 ou aceleradores dedicados), de modo a definir o hardware mínimo necessário para atender aos requisitos de tempo real.

O objetivo é determinar qual combinação de hardware e técnicas de otimização é adequada ao projeto, identificando gargalos e os limites de viabilidade da execução embarcada.

#### Etapa 10: Consolidação dos Resultados e Produção Científica

Nesta etapa serão executadas as seguintes atividades:

- Organização dos dados experimentais;
- Elaboração de relatórios técnicos;
- Produção de documentação do sistema desenvolvido;
- Preparação de artigo científico;
- Preparação de material para apresentação no Congresso de Iniciação Científica da Universidade de Brasília.

A gestão do projeto adotará práticas de gerenciamento inspiradas nas metodologias PMI/PMBOK (PMI, 2021) e Scrum (Cruz, 2013), utilizando reuniões periódicas para acompanhamento das atividades, avaliação dos resultados e definição das ações corretivas necessárias. O desenvolvimento será conduzido de forma incremental, permitindo a evolução contínua do protótipo e a validação progressiva das hipóteses de pesquisa.

### 4) Bibliografia básica

- AMEEN, M.; VOKHIDOV, H. Autonomous Mobile Robot Navigation: Tracking Problem. 2024.
- DEWANTORO, R. et al. Comparative Study of Computer Vision Based Line Followers Using Raspberry Pi and Jetson Nano. 2021.
- PASTRANA TRIANA, M. A. Estancia de investigación en circuitos embebidos y sistemas en chip aplicados a robótica y control. 2019.
- KIM, D.; PRAKAPOVICH, A. Optimization of the PID Coefficients for the Line-Follower Mobile Robot Controller Employing Genetic Algorithm. 2021.
- OGUTEN, T.; KABAS, O. PID Controller Optimization for Low-Cost Line Follower Robots. 2021.
- RIHEM, F.; ALJALOUD, K. Vision Navigation Based PID Control for Line Tracking Robot. 2023.
- VARGAS TORRES, J.; SANTIAGO-PAZ, J. Robot Seguidor de Línea Basado en Visión Artificial con ROS y OpenCV. 2019.
- PMI. Guia de Conhecimento em Gerenciamento de Projetos (GUIA PMBOK). 7. ed. Project Management Institute (PMI), Pennsylvania, 2021.
- Cruz, F. Scrum e PMBOK unidos no gerenciamento de projetos. Editora BRASPORT, São Paulo, 2013.
- M. Voellmy and M. Ehrhardt: ExoMy: A Low Cost 3D Printed Rover. International Symposium on Artificial Intelligence, Robotics and Automation in Space (i-SAIRAS), 2020.

---

## PLANO DE TRABALHO

### Título do Plano de Trabalho

Desenvolvimento de um Robô Seguidor de Linha Autônomo com Controle PID Otimizado por Algoritmos Bioinspirados e Navegação Baseada em Visão Computacional Embarcada

**Aluno:** Felipe das Neves Freire
**Matrícula:** 20/2046102

### 1. Adequação do plano de trabalho ao nível de Iniciação Científica e ao projeto de pesquisa do(a) orientador(a)

#### Contextualização

Robôs móveis autônomos vêm sendo amplamente utilizados em aplicações industriais, logísticas, agrícolas, de inspeção e exploração, impulsionando pesquisas voltadas ao desenvolvimento de sistemas de navegação cada vez mais robustos, eficientes e adaptáveis. Entre os desafios clássicos da robótica móvel destaca-se a capacidade de navegar autonomamente em ambientes estruturados e não estruturados, mantendo precisão e estabilidade mesmo diante de perturbações externas e mudanças nas condições operacionais.

Os robôs seguidores de linha constituem uma plataforma amplamente utilizada para estudo e validação de técnicas de controle, percepção e navegação autônoma. Tradicionalmente, esses sistemas utilizam sensores de refletância associados a controladores PID para correção da trajetória. Embora essa abordagem apresente baixo custo computacional e simplicidade de implementação, seu desempenho pode ser limitado em situações que envolvem variações de iluminação, mudanças nas características da pista, curvas acentuadas ou velocidades elevadas, tornando necessária a investigação de métodos mais avançados de percepção e controle.

O projeto Robô Bio surgiu inicialmente como trabalho final da disciplina Fundamentos de Sistemas Embarcados (FSE) da Universidade de Brasília, utilizando controle PID clássico, sensores de refletância e telemetria baseada na plataforma ThingsBoard para monitoramento remoto. Em sua segunda versão, o projeto evoluiu para uma nova arquitetura mecânica inspirada no rover open-source ExoMy, desenvolvido pelo Planetary Robotics Laboratory da European Space Agency (ESA) como plataforma modular de pesquisa e ensino em robótica móvel. Essa evolução proporcionou maior robustez estrutural, modularidade e capacidade de expansão para integração de novos sensores e algoritmos.

A presente proposta visa desenvolver a segunda geração do Robô Bio, transformando-o em uma plataforma experimental para pesquisa em robótica móvel autônoma. A evolução proposta consiste na incorporação de visão computacional embarcada utilizando Raspberry Pi e OpenCV para identificação e segmentação da pista em tempo real, associada à aplicação de algoritmos bioinspirados para ajuste automático dos parâmetros do controlador PID.

Além da substituição ou complementação dos sensores tradicionais por percepção visual, o sistema será capaz de coletar e armazenar dados de telemetria durante a navegação, permitindo análises quantitativas do comportamento do robô e do desempenho dos algoritmos implementados. A combinação entre visão computacional, sistemas embarcados e otimização bioinspirada permitirá investigar estratégias de controle inteligente capazes de melhorar a precisão, estabilidade e velocidade de navegação em comparação com abordagens convencionais.

Dessa forma, o Robô Bio passa a atuar não apenas como um robô seguidor de linha, mas como uma plataforma modular de pesquisa para desenvolvimento e validação de técnicas de navegação autônoma, controle inteligente e inteligência artificial aplicada à robótica móvel.

#### Justificativa

A sintonia adequada dos ganhos proporcional (Kp), integral (Ki) e derivativo (Kd) constitui um dos principais desafios associados à utilização de controladores PID em sistemas robóticos. Métodos convencionais de ajuste, como Ziegler-Nichols ou sintonia manual, frequentemente exigem elevado esforço experimental e podem produzir resultados insatisfatórios quando aplicados a sistemas sujeitos a não linearidades, ruídos e mudanças nas condições de operação.

Nesse contexto, algoritmos bioinspirados têm se destacado como alternativas promissoras para otimização automática de parâmetros de controle. Técnicas como Particle Swarm Optimization (PSO) e Differential Evolution (DE) apresentam elevada capacidade de exploração do espaço de busca e têm sido empregadas com sucesso na sintonia de controladores aplicados à robótica móvel, reduzindo a dependência de ajustes empíricos e melhorando métricas de desempenho como erro de rastreamento, estabilidade e tempo de acomodação.

Paralelamente, o avanço dos sistemas embarcados de baixo custo tornou viável a utilização de visão computacional em plataformas robóticas compactas. O uso de câmeras embarcadas permite obter informações mais ricas sobre o ambiente quando comparado aos sensores discretos tradicionais, possibilitando a identificação da trajetória por meio de técnicas de processamento digital de imagens, segmentação e extração de características visuais.

A integração entre visão computacional e controle inteligente representa atualmente uma das principais tendências de pesquisa em robótica móvel autônoma, uma vez que permite ampliar a capacidade de percepção do ambiente e aumentar a adaptabilidade dos sistemas de navegação. Além disso, a utilização de plataformas abertas e modulares, inspiradas em projetos como o ExoMy, favorece a reprodutibilidade científica e a continuidade de pesquisas futuras.

Dessa forma, o presente trabalho busca investigar a aplicação conjunta de técnicas de visão computacional embarcada, otimização bioinspirada e controle PID em uma plataforma robótica modular, contribuindo para o avanço das pesquisas nas áreas de sistemas embarcados, inteligência artificial, controle inteligente e robótica móvel autônoma. Os resultados obtidos poderão servir como base para futuros estudos envolvendo aprendizado de máquina embarcado, navegação autônoma avançada, fusão sensorial e sistemas ciberfísicos.

#### Hipótese Científica

A hipótese central é que algoritmos bioinspirados (PSO e DE) convergem para conjuntos de parâmetros do controlador PID (Kp, Ki, Kd) que reduzem o erro quadrático médio (RMSE) de rastreamento da trajetória em pelo menos X% em relação à sintonia clássica de Ziegler-Nichols e à sintonia manual, mantendo a estabilidade do sistema em cenários de iluminação variável detectados por visão computacional embarcada. O percentual de referência será consolidado após o estabelecimento da linha de base experimental.

A hipótese será testada de forma quantitativa, comparando as métricas de desempenho (Seção *Metodologia*, Etapas 6 a 8) entre os controladores ajustados manualmente, por métodos clássicos e por otimização bioinspirada, com tratamento estatístico dos resultados.

#### Objetivo Geral

Desenvolver e validar uma plataforma robótica móvel autônoma baseada em visão computacional embarcada e controle PID otimizado por algoritmos bioinspirados para navegação em pistas delimitadas visualmente.

#### Objetivos Específicos

- Evoluir o Robô Bio para sua segunda geração, baseada em arquitetura modular inspirada no rover ExoMy;
- Modelar, fabricar e integrar os componentes mecânicos do robô utilizando técnicas de manufatura aditiva;
- Desenvolver a eletrônica embarcada necessária para controle, aquisição de dados e comunicação;
- Implementar sistema de visão computacional utilizando Raspberry Pi Camera e OpenCV;
- Desenvolver algoritmos para detecção, segmentação e rastreamento da pista em tempo real;
- Implementar e validar controladores PID para navegação autônoma;
- Desenvolver e implementar algoritmos bioinspirados, com foco em PSO e Differential Evolution, para ajuste automático dos parâmetros PID;
- Desenvolver infraestrutura de telemetria para monitoramento e armazenamento dos dados experimentais;
- Comparar o desempenho entre métodos tradicionais de sintonia PID e métodos baseados em otimização bioinspirada;
- Avaliar métricas de desempenho como erro lateral, RMSE da trajetória, estabilidade, velocidade média, tempo de percurso e taxa de sucesso da navegação;
- Analisar o desempenho computacional do sistema embarcado com enfase no uso de CPU e memória, e determinar os requisitos de hardware necessários para a execução em tempo real da visão computacional, do controle e da otimização bioinspirada;
- Produzir documentação técnica e científica dos resultados obtidos;
- Estabelecer uma plataforma experimental que possa ser utilizada em futuras pesquisas nas áreas de robótica móvel, inteligência artificial e sistemas embarcados.

### 2. Viabilidade de execução (recursos e infraestrutura)

A execução do projeto é viável devido à infraestrutura disponível nos laboratórios da Universidade de Brasília (UnB), à experiência acumulada durante o desenvolvimento das versões anteriores do Robô Bio e à disponibilidade de equipamentos utilizados em pesquisa nas áreas de robótica móvel, sistemas embarcados, manufatura aditiva e inteligência artificial aplicada.

O Robô Bio encontra-se atualmente em fase de modelagem mecânica e integração de sistemas, possuindo arquitetura modular que permite futuras expansões de hardware e software. O desenvolvimento do protótipo utilizará recursos já disponíveis na universidade, bem como componentes adquiridos especificamente para a pesquisa.

#### Especificação de Bens de Custeio

- Materiais e insumos necessários à realização do projeto, incluindo filamentos para impressão 3D (PLA e PETG), componentes eletrônicos, placas de desenvolvimento, sensores, motores, baterias e dispositivos de comunicação.

#### Especificação de Bens de Capital

- Plataformas embarcadas de processamento (ex.: Raspberry Pi Zero 2W e modelos superiores), bem como acessórios para processamento embarcado e execução dos algoritmos de visão computacional a definição final do hardware será orientada pela análise de desempenho computacional prevista na metodologia.
- Câmera embarcada compatível com Raspberry Pi para aquisição de imagens e processamento visual da pista.
- Impressoras 3D para fabricação de componentes estruturais do robô.
- Estações de desenvolvimento para programação, análise de dados e treinamento dos algoritmos.
- Instrumentação eletrônica para montagem, testes e validação dos sistemas embarcados.
- Equipamentos de comunicação e telemetria para monitoramento e aquisição de dados experimentais.

#### Infraestrutura Disponível

A infraestrutura disponível em diversos laboratórios da UnB para execução dos experimentos do projeto pode ser observada a seguir:

- Impressoras 3D para fabricação rápida de protótipos e componentes estruturais;
- Laboratórios de sistemas embarcados para desenvolvimento eletrônico e integração de hardware;
- Computadores de alto desempenho para processamento de imagens e desenvolvimento de algoritmos;
- Equipamentos para prototipagem eletrônica, soldagem e montagem de circuitos;
- Instrumentação para caracterização e análise de sinais;
- Espaços controlados para realização de testes experimentais com robôs móveis;
- Ferramentas de modelagem CAD para projeto mecânico e simulações;
- Infraestrutura de rede para comunicação, monitoramento remoto e armazenamento de dados experimentais.

Os recursos disponíveis permitem a realização de todas as etapas previstas no plano de trabalho, incluindo modelagem mecânica, fabricação do protótipo, implementação dos algoritmos de visão computacional, desenvolvimento dos controladores PID inteligentes, coleta de dados experimentais e validação dos resultados obtidos.

### 3. Cronograma de execução

**Mês 01:** Revisão bibliográfica: Robótica móvel autônoma; Sistemas embarcados; Controle PID aplicado a robôs seguidores de linha.

**Mês 02:** Revisão bibliográfica: Algoritmos bioinspirados para otimização; Particle Swarm Optimization (PSO); Differential Evolution (DE); Aplicações em controle inteligente.

**Mês 03:** Revisão bibliográfica: Visão computacional embarcada; Processamento digital de imagens; OpenCV; Navegação autônoma baseada em câmera.

**Mês 04:** Modelagem mecânica e fabricação dos componentes do Robô Bio utilizando manufatura aditiva; montagem estrutural do protótipo.

**Mês 05:** Integração eletrônica do sistema embarcado; instalação da Raspberry Pi, câmera, controladores de motores, sensores e sistema de alimentação.

**Mês 06:** Implementação e validação do controlador PID clássico; aquisição de dados experimentais e ajuste inicial dos parâmetros de controle.

**Mês 07:** Desenvolvimento do sistema de visão computacional para detecção e segmentação da pista; processamento de imagens em tempo real utilizando OpenCV.

**Mês 08:** Integração entre visão computacional e sistema de controle; realização dos primeiros testes de navegação autônoma; análise inicial de desempenho computacional analisando uso de CPU e memória.

**Mês 09:** Implementação dos algoritmos bioinspirados para otimização automática dos parâmetros PID; definição das métricas de desempenho e função objetivo.

**Mês 10:** Execução dos experimentos comparativos entre PID convencional e PID otimizado; coleta de telemetria e análise de desempenho em diferentes trajetórias.

**Mês 11:** Tratamento estatístico dos resultados; avaliação da estabilidade, precisão, velocidade e robustez do sistema; análise de desempenho computacional e definição dos requisitos de hardware; redação do relatório técnico-científico.

**Mês 12:** Consolidação dos resultados obtidos; preparação de artigo para publicação em evento e/ou periódico técnico-científico; preparação da apresentação para o Congresso de Iniciação Científica da UnB.

### 5. Justificativa elaborada pelo(a) orientador(a) acerca das competências e habilidades do aluno para desenvolver as atividades do plano de trabalho.

Tendo em vista as seguintes informações apresentadas pelo aluno ou que constam no curriculum vitae lattes do discente:

No presente momento o discente é graduando em Engenharia de Software e já integralizou 2645 horas em seu histórico. Possui experiência com eletrônica e software embarcado.

O aluno é engajado em atividades extracurriculares. É atualmente líder de projeto da Equipe do Seguidor de Linha (Titans) e também coordena a equipe de desenvolvimento do sistema Web da equipe.

Desta forma, justifico que o referido aluno tem qualidades e a formação básica para poder desenvolver um trabalho de iniciação científica.
