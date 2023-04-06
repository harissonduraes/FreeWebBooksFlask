import click
from projetoFlask.ext.database import db
from projetoFlask.ext.auth import create_user
from projetoFlask.ext.database import TypeProduct, Product, Livro, Pagina


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    tp = [
            TypeProduct(
                id=1,
                description="Tipo produto 1"),
            TypeProduct(
                id=2,
                description="Tipo produto 2")
        ]


    lv = [
            Livro(
                id=1,
                name="Clean Code",
                image_url="https://media.licdn.com/dms/image/C4D12AQElMcNEch38WQ/article-cover_image-shrink_720_1280/0/1645152091261?e=2147483647&v=beta&t=cBzmomM3hef1Mcpbw5O9Afs_1zABFkeoHv_OoQJPRKE",
                description="Mesmo um código ruim pode funcionar. Mas se ele não for limpo, pode acabar com uma empresa de desenvolvimento. Perdem-se a cada ano horas incontáveis e recursos importantes devido a um código mal escrito."),
            Livro(
                id=2,
                name="Clean Code",
                image_url="https://media.licdn.com/dms/image/C4D12AQElMcNEch38WQ/article-cover_image-shrink_720_1280/0/1645152091261?e=2147483647&v=beta&t=cBzmomM3hef1Mcpbw5O9Afs_1zABFkeoHv_OoQJPRKE",
                description="Mesmo um código ruim pode funcionar. Mas se ele não for limpo, pode acabar com uma empresa de desenvolvimento. Perdem-se a cada ano horas incontáveis e recursos importantes devido a um código mal escrito. Mas não precisa ser assim.O renomado especialista em software, Robert C. Martin, apresenta um paradigma revolucionário com Código limpo"),
            Livro(
                id=3,
                name="Arquitetura Moderna",
                image_url="https://engsoftmoderna.info/figs/capa/capa-3d-principal.jpg",
                description="Engenharia de Software Moderna é um livro-texto destinado a alunos de cursos de graduação em Computação. Pode ser lido também por profissionais que bu"),
            Livro(
                id=4,
                name="Arquitetura Limpa",
                image_url="https://m.media-amazon.com/images/I/41T8NdKFqEL._SY344_BO1,204,203,200_QL70_ML2_.jpg",
                description="As regras universais de arquitetura de software aumentam dramaticamente a produtividade dos desenvolvedores ao longo da vida dos sistemas de software.")
    ]

    pg = [
            Pagina(
                id = 1,
                number = 1,
                content = "Mesmo um código ruim pode funcionar. Mas se ele não for limpo, pode acabar com uma empresa de desenvolvimento. Perdem-se a cada ano horas incontáveis e recursos importantes devido a um código mal escrito",
                id_livro = 1),
            Pagina(
                id = 2,
                number = 2,
                content = "Código limpo está divido em três partes. Na primeira há diversos capítulos que descrevem os princípios, padrões e práticas para criar um código limpo.A segunda parte consiste em diversos casos de estudo de complexidade cada vez maior. Cada um é um exercício para limpar um código – transformar o código base que possui alguns problemas em um melhor e ef",
                id_livro = 1),
            Pagina(
                id = 3,
                number = 1,
                content = "Após ler este livro os leitores saberão:✔ Como distinguir um código bom de um ruim✔ Como escrever códigos bons e como transformar um ruim em um bom✔ Como criar bons nomes, boas funções, bons objetos e boas classes✔ Como formatar o código para ter uma legibilidade máxima✔ Como implementar completamente o tratamento de erro sem obscurecer a lógica✔ Como aplicar testes de unidade e praticar o desenvolvimento dirigido a testesEste livro é essencial para qualquer desenvolvedor, engenheiro de software, gerente de projeto, líder de equipes ou analistas de sistemas com interesse em construir códigos melhores.",
                id_livro = 2),
            Pagina(
                id = 4,
                number = 1,
                content = "Página principal do livro Compre na Amazon ou Casas Bahia Veja também os cursos de extensão a distância Engenharia de Software Moderna (48 horas) e Teste de Software (20 horas), oferecidos pelo DCC/UFMG. Engenharia de Software Moderna Marco Tulio Valente Prefácio 🔗 A inutilidade dos prefácios é um lugar comum da história dos prefácios, portanto serei breve. – Eduardo Giannetti A ideia de escrever este livro surgiu no início de 2019, quando fui alocado para ministrar a disciplina Engenharia de Software, do Bacharelado em Ciência da Computação, da UFMG. Para preparar o curso, comecei com uma análise dos principais livros de Engenharia de Software. Para minha surpresa, percebi que eles tinham mudado pouco desde que cursei a disciplina na minha graduação há mais de 25 anos! Meu objetivo era escolher um livro que permitisse, no início de uma aula, dizer para os alunos: hoje vamos estudar tal assunto, que corresponde a tal capítulo do livro-texto. No final da aula, gostaria de sugerir aos alunos: para fixar a matéria que acabamos de ver, sugiro que façam tais exercícios. No entanto, infelizmente, não encontrei esse livro.",
                id_livro = 3),
            Pagina(
                id = 5,
                number = 1,
                content = "Domine os princípios essenciais do design de software para abordar função, separação de componentes e gestão de dados;Veja como os paradigmas de programação impõem disciplina ao restringirem as ações dos desenvolvedores;Saiba identificar o que é crucialmente importante e o que é apenas um “detalhe”;Implemente estruturas ótimas e de alto nível para web, banco de dados, thick-client, console e aplicativos incorporados;Defina limites e camadas adequadas e organize os componentes e serviços;Saiba por que designs e arquiteturas dão errado e como prevenir (ou corrigir) essas falhas.",
                id_livro = 4),
    ]


    data = [
        tp[0],
        tp[1],
        Product(
            id=1, 
            name="Produto 1", 
            price="10.00", 
            description="Produto 1 para teste",
            type_id=tp[0].id),
        Product(
            id=2, 
            name="Produto 2", 
            price="20.00", 
            description="Produto 2 para teste",
            type_id=tp[0].id),
        Product(
            id=3, 
            name="Produto 3", 
            price="30.00", 
            description="Produto 3 para teste",
            type_id=tp[1].id),
    ]
    #db.session.bulk_save_objects(tp)
    #db.session.bulk_save_objects(data)
    db.session.bulk_save_objects(lv)
    db.session.bulk_save_objects(pg)
    db.session.commit()
    return  Livro.query.all(), Pagina.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    def add_user(username, password):
        """Adds a new user to the database"""
        return create_user(username, password)
