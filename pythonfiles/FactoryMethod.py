from abc import ABC, abstractmethod

# 抽象产品
class AbstractProduct(ABC):
    @abstractmethod
    def product_name(self):
        pass

# 具体产品A
class ProductA(AbstractProduct):
    def product_name(self):
        return "Product A"

# 具体产品B
class ProductB(AbstractProduct):
    def product_name(self):
        return "Product B"

# 抽象工厂
class AbstractFactory(ABC):
    @abstractmethod
    def create_product(self):
        pass

# 具体工厂A
class ConcreteFactoryA(AbstractFactory):
    def create_product(self):
        return ProductA()

# 具体工厂B
class ConcreteFactoryB(AbstractFactory):
    def create_product(self):
        return ProductB()

# 客户端代码
def client_code(factory):
    product = factory.create_product()
    print("Product:", product.product_name())

# 使用具体工厂A创建产品
factory_a = ConcreteFactoryA()
client_code(factory_a)

# 使用具体工厂B创建产品
factory_b = ConcreteFactoryB()
client_code(factory_b)
