# CRUD_Gerenciador_Academico

# 🎓 Sistema de Gestão Acadêmica (CRUD)

Um sistema completo de gestão académica desenvolvido em **Python**. O projeto foi estruturado utilizando o paradigma procedural, aplicando conceitos avançados de reutilização de código através de funções genéricas para manipulação de coleções de dados (estruturadas como dicionários dentro de listas).

Este software foi desenvolvido como objeto de estudo e validação prática de lógica de programação e estruturas de dados, contando com a orientação e mentoria do professor da unidade curricular.

## 🚀 Diferencial Técnico da Arquitetura

Em vez de criar funções de inserção, listagem, atualização e eliminação repetitivas para cada entidade, o sistema utiliza uma **abordagem dinâmica**. Através das funções genéricas `inclusao()`, `listagem()`, `atualizacao()` e `exclusao()`, o sistema recebe a lista alvo e os campos específicos via parâmetro (`["nome", "cpf"]`). 

Isto reduz drasticamente a duplicidade de código (princípio DRY - *Don't Repeat Yourself*) e facilita a escalabilidade do sistema.

## 📂 Módulos de Gestão (Entidades)

O sistema faz o mapeamento e controlo de 5 pilares fundamentais de uma instituição de ensino:
1. **Estudantes:** Registo de alunos com Nome e CPF.
2. **Professores:** Registo do corpo docente com Nome e CPF.
3. **Disciplinas:** Cadastro das matérias ofertadas pela instituição.
4. **Turmas:** Criação de agrupamentos de alunos associados a um identificador.
5. **Matrículas:** Vínculo direto que conecta um Estudante (`id_estudante`) a uma Turma (`id_turma`).

## 📊 Estrutura dos Dados (Dicionários)

Cada registo é guardado como um dicionário com chaves dinâmicas e um ID gerado automaticamente. Exemplo de estrutura em memória:

```python
# Exemplo de dicionário da entidade Estudante
{
    "codigo": 1,
    "nome": "Lucas Silva",
    "cpf": "123.456.789-00"
}

# Exemplo de dicionário da entidade Matrícula
{
    "codigo": 1,
    "id_estudante": "1",
    "id_turma": "1"
}
