from abc import ABC, abstractmethod

# 抽象产品A
class AbstractProductA(ABC):
    @abstractmethod
    def product_name(self):
        pass

# 具体产品A1
class ProductA1(AbstractProductA):
    def product_name(self):
        return "Product A1"

# 具体产品A2
class ProductA2(AbstractProductA):
    def product_name(self):
        return "Product A2"

# 抽象产品B
class AbstractProductB(ABC):
    @abstractmethod
    def product_name(self):
        pass

# 具体产品B1
class ProductB1(AbstractProductB):
    def product_name(self):
        return "Product B1"

# 具体产品B2
class ProductB2(AbstractProductB):
    def product_name(self):
        return "Product B2"

# 抽象工厂
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

# 具体工厂1
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()

# 具体工厂2
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ProductA2()

    def create_product_b(self):
        return ProductB2()

# 客户端代码
def client_code(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print("Product A:", product_a.product_name())
    print("Product B:", product_b.product_name())

# 使用具体工厂1创建产品
factory1 = ConcreteFactory1()
client_code(factory1)

# 使用具体工厂2创建产品
factory2 = ConcreteFactory2()
client_code(factory2)
