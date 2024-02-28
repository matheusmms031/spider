# SpiderScan

O programa é um scanner de aplicações web completo, ele descobre rotas do site alvo usando uma *wordlist* como o (Gobuster)[] porém também possuí outras utilidades como: 

1. Recolher links vulneráveis em cada rota.
2. Testa ataques XSS.
3. Identifica versão do OS e etc.

## Sua eficiência

A aplicação possuí uma eficiência considerável em relação a outros concorrentes, porém continua atrás de certos outros pelo o uso do Python, mas como ele utiliza o aiohttp e a biblioteca asyncio acaba sendo bem eficiente por si só.