class Carrinho:
    def __init__(self) -> None:
        self._produtos = []
        
    def total(self):
        return sum([p.preco for p in self._produtos])

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()
        
    def inserir_produtos(self, *produtos):
        self._produtos.extend(produtos)
        
class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome 
        self.preco = preco
        
        
carrinho = Carrinho()
p1, p2 = Produto('arroz 1kg', 6.77), Produto('macarrao 500g', 2.64)
carrinho.inserir_produtos(p1, p2)

carrinho.listar_produtos()
print(carrinho.total())