# 💼 Boas-vindas ao Projeto Job Insigths!
Este projeto foi desenvolvido durante o curso da [Trybe](https://www.betrybe.com/).

    > Projeto 33 🚀
    > Módulo - Ciência da Computação
    > Bloco 33 - Introdução à Python

## 📈 Sobre o projeto
Neste projeto foram implementadas análises a partir de um conjunto de dados sobre empregos. O objetivo era realizar a implementação de algumas funções capazes de fazerem manipulações com esses dados.

Tais implementações foram incorporadas a um aplicativo Web desenvolvido com **Flask** (um framework web muito popular na comunidade Python) que já veio implementado no projeto pela Trybe. Também foram escritos testes para a implementação de uma análise de dados.

Também foi desenvolvido um teste para validar o retorno de uma função previamente implementada pela Trybe.

Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br//) e obtidos através do [Kaggle](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data), uma plataforma que disponibliza conjuntos de dados para cientistas de dados.


## 📎Stacks utilizadas

**Back-end:** Python 3, Flask

## 📃 Lista de requisitos 
À seguir, listo todos os requisitos solicitados no projeto para que fossem desenvolvidos por mim.

`Obrigatórios`

- ✅ 1 - Implementar a função read
- ✅ 2 - Implementar a função get_unique_job_types
- ✅ 3 - Implementar a função get_unique_industries
- ✅ 4 - Implementar a função get_max_salary
- ✅ 5 - Implementar a função get_min_salary
- ✅ 6 - Implementar a função filter_by_job_type
- ✅ 7 - Implementar a função filter_by_industry
- ✅ 8 - Implementar a função matches_salary_range
- ✅ 9 - Implementar a função filter_by_salary_range
- ✅ 10 - Implementar um teste para a função sort_by

`Requisitos bônus`

- 🔲 11 - Implementar a página de um job
#### 📂 Estrutura de pastas dos arquivos implementados

```
.
├── src
│   ├── insights.py
│   ├── jobs.py
├── tests
│   ├── sorting
│   │   └── test_sorting.py
```
## ⚙️ Rodando localmente

Clone o projeto

```bash
  git clone git@github.com:aicitelks/project-job-insights.git
```

Entre no diretório do projeto

```bash
  cd project-job-insights
```

Crie o ambiente virtual para o projeto
```bash
  python3 -m venv .venv && source .venv/bin/activate
```

Instale as dependências

```bash
  python3 -m pip install -r dev-requirements.txt
```

Rode a aplicação **Flask** para visualizar no navegador o resultado do desenvolvimento das funções

```bash
  flask run
```

E acesse o site gerado pelo Flask `http://localhost:5000`


### 🚧 Implementações futuras
- Desenvolver a página de um job (requisito ônus)

## 🏆 Nota do projeto na Trybe

![Nota do projeto na Trybe](/job_insights.jpg)
___

#### 💻 Desenvolvido por [@aicitelks](https://github.com/aicitelks/) 📆 2022 🔗 [LinkedIn](https://www.linkedin.com/in/leticiacastro87)