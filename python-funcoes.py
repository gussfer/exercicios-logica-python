def calculaMedia(n1, n2):
    media = (n1+n2)/2
    return media
print("Sua média é:",calculaMedia(8,9))

def calcula_media(*args):
    media = (sum(args)/len(args))
    return media
print("Sua média é:",calcula_media(8,9))
