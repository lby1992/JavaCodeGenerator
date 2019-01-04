from .preset_constants import *


class JavaElement:
    def __init__(self, name, element_type, return_type, visibility, is_static, inherit_modifier, initialization_value,
                 description, annotations):
        """
        代表java元素
        :param name: 元素名称，例如类名、字段名等
        :param element_type: 元素类型，例如类、字段、方法等
        :param return_type: 返回类型。当元素类型无需返回时为None
        :param visibility: 可见性修饰
        :param is_static: 是否静态
        :param inherit_modifier: 继承性修饰。没有为None，如构造器
        :param initialization_value: 初始化的值。没有为None，如方法
        :param description: 用来生成javadoc
        :param annotations: 注解
        """
        self.name = name
        self.member_type = element_type
        self.return_type = return_type
        self.visibility = visibility
        self.is_static = is_static
        self.inherit_modifier = inherit_modifier
        self.initialization_value = initialization_value
        self.description = description
        self.annotations = annotations


class JavaPackage(JavaElement):
    def __init__(self, name, description=None):
        super().__init__(name, element_type=TYPE_PACKAGE, description=description, return_type=None, visibility=None,
                         is_static=False, inherit_modifier=None, initialization_value=None, annotations=None)

    def add_package(self):
        pass


class JavaType(JavaElement):
    """代表java中的类型"""
    def __init__(self, name, package_name=None, class_type=TYPE_CLASS, visibility=VISIBILITY_PUBLIC,
                 inherit_modifier=INHERIT_DEFAULT, is_static=False, description=None, extended_class=None,
                 implemented_interfaces=None, members=None, annotations=None):
        super().__init__(name=name, element_type=class_type, return_type=None, visibility=visibility,
                         is_static=is_static, inherit_modifier=inherit_modifier, initialization_value=None,
                         description=description, annotations=annotations)
        self.package_name = package_name
        self.members = members
        self.extended_class = extended_class
        self.implemented_interfaces = implemented_interfaces

    def add_member(self, member):
        if not self.members:
            self.members = list()
        list.append(self.members, member)


class JavaConstructor(JavaElement):
    """代表java中的构造器"""
    def __init__(self, name, visibility=VISIBILITY_PUBLIC, description='Generated Java constructor.', annotations=None):
        super().__init__(name, element_type=TYPE_CONSTRUCTOR, return_type=None, visibility=visibility,
                         inherit_modifier=None, is_static=False, description=description, initialization_value=None,
                         annotations=annotations)


class JavaField(JavaElement):
    """代表java中的字段"""
    def __init__(self, name, return_type, visibility=VISIBILITY_PRIVATE, is_static=False, annotations=None,
                 inherit_modifier=INHERIT_DEFAULT, description='Generated Java filed.', initialization_value=None):
        super().__init__(name=name, element_type=TYPE_FIELD, return_type=return_type, visibility=visibility,
                         is_static=is_static, inherit_modifier=inherit_modifier, description=description,
                         initialization_value=initialization_value, annotations=annotations)


class JavaConstant(JavaField):
    """代表Java中的常量"""
    def __init__(self, name, return_type, initialization_value, visibility, description='Generated Java constant.'):
        super().__init__(name=name, return_type=return_type, inherit_modifier=INHERIT_FINAL, is_static=True,
                         description=description, initialization_value=initialization_value, visibility=visibility)


class JavaMethod(JavaElement):
    """代表java中的方法"""
    def __init__(self, name, visibility, inherit_modifier=INHERIT_DEFAULT, is_static=False, return_type=None,
                 description='Generated Java method.', annotations=None, params=None):
        super().__init__(name, TYPE_METHOD, visibility=visibility, inherit_modifier=inherit_modifier,
                         return_type=return_type, description=description, annotations=annotations,
                         initialization_value=None, is_static=is_static)
        self.params = params

    def add_parameter(self, parameter):
        if not self.params:
            self.params = list()
        list.append(self.params, parameter)


class JavaParameter(JavaElement):
    def __init__(self, name, return_type, visibility, description=None, annotations=None):
        super().__init__(name, element_type=TYPE_PARAMETER, return_type=return_type, visibility=visibility,
                         is_static=False, inherit_modifier=INHERIT_DEFAULT, initialization_value=None,
                         description=description, annotations=annotations)


class JavaAnnotation(JavaType):
    def __init__(self, name, package_name=None, description='Generated Java annotation.', annotations=None):
        super().__init__(name, class_type=TYPE_ANNOTATION, package_name=package_name, description=description,
                         annotations=annotations)
