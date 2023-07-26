import OpenGL.GL as gl
from OpenGL.GL import shaders


class lazy_class_attribute(object):
    def __init__(self, function):
        self.fget = function

    def __get__(self, obj, cls):
        value = self.fget(obj or cls)
        # note: クラスレベルのアクセスか、インスタンスレベルの
        #       アクセスかに関係なく、すべてをクラスオブジェクト
        #       に格納する        setattr(cls, self.fget.__name__, value)
        return value


class ObjectUsingShaderProgram(object):
    # 座標をそのまま変換せずに出力するバーテックスシェーダ
    VERTEX_CODE = """ 
        #version 330 core 
        layout(location = 0) in vec4 vertexPosition; 
        void main(){ 
            gl_Position =  vertexPosition; 
        } 
    """
    # すべてのピクセルを白色に塗るフラグメントシェーダ
    FRAGMENT_CODE = """ 
        #version 330 core 
        out lowp vec4 out_color; 
        void main(){ 
            out_color = vec4(1, 1, 1, 1); 
        } 
    """

    @lazy_class_attribute
    def shader_program(self):
        print("コンパイル中!")
        return shaders.compileProgram(
            shaders.compileShader(self.VERTEX_CODE, gl.GL_VERTEX_SHADER),
            shaders.compileShader(self.FRAGMENT_CODE, gl.GL_FRAGMENT_SHADER),
        )
