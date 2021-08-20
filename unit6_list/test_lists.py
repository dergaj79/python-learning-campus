## unit 6 lists

movies = [
            ['titanic',1997,'leonardo dicaprio','Kate winslet',3.25,True],
            ['star wars',2001,'actar name1','actar name2',3.4,False],
            ['pocahonts',2010,"actar1","actar2",3.0,False],
            ['E.T.',1981,'actar1','actar2',4,False],
            ['Forrest Gump',2000,'actar1','actar2',2,False]
        ]
print(type(movies[0]))
print(movies[2][3])

def cool_trick():
    cool_trick = [1,2,3,4,5]
    a,b,c,d,e = cool_trick
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


def main():
    cool_trick()

if __name__ == "__main__":
    main()