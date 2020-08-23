print("""
Mad Libs Generator!

Enter a number:
1: Romeo and Juiet
2: Bee Movie
3: FitGram Pacer Test
""")
texts = [juliet, beemovie, fitgram]
choice = texts[int(input()) - 1]
juliet = f"""O Romeo, Romeo, wherefore art thou Romeo?
Deny thy father and refuse thy name.
Or if thou wilt not, be but sworn my love
And I’ll no longer be a Capulet.
‘Tis but thy name that is my enemy:
Thou art thyself, though not a Montague.
What’s Montague? It is nor hand nor foot
Nor arm nor face nor any other part
Belonging to a man. O be some other name.
What’s in a name? That which we call a rose
By any other name would smell as sweet;
So Romeo would, were he not Romeo call’d,
Retain that dear perfection which he owes
Without that title. Romeo, doff thy name,
And for that name, which is no part of thee,
Take all myself.
"""
juliet_libs = "name noun noun noun noun verb adjective noun verb".split()
beemovie = """accor
"""
fitgram = """THe
"""
