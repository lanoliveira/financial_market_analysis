# Projeto

1º passo - Cria a imagem do crawler (é necessário estar no diretório do projetoDocker):
    
    docker build --tag crawler .

2º passo - Cria a imagem do streamlit (é necessário estar no diretório do simuladorBazin):
    
    docker build --tag streamlit .

3º passo - Cria o container do projeto (é necessário estar no diretório do financial_market_analysis):
    
    docker compose up --build

4º passo - Acessar o streamlit (as informações só estarão disponíveis após o crawler terminar de coletar os dados):
    
    http://localhost:8501/
