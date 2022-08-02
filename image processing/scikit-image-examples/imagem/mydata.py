from skimage import io

root = "C:/Users/leyrisvan/Processamento-de-imagens/scikit-image-examples/models/"

def coelho():
    imagem = io.imread(root + 'coelho.png')
    return imagem

def gorro():
    imagem = io.imread(root + 'gorro.png')
    return imagem


def boneco():
   imagem = io.imread(root + 'boneco.png')
    return imagem


def flamengo():
   imagem = io.imread(root + 'flamengo.png')
    return imagem


def noel():
    imagem= io.imread(root + 'noel.png')
    return imagem

def hiena():
   imagem = io.imread(root + 'hiena.png')
    return imagem

def resmag():
   imagem = io.imread(root + 'resmag.jpg')
    return imagem
