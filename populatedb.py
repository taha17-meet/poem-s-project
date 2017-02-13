from databases import *
engine = create_engine('sqlite:///poems.db')
Base.metadata.bind= engine
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()



### Initialize database with entries ###
if session.query(Poem).filter_by(name = '''You're My Everything''' ).all() == []:
	poemA1 = Poem(name='''You're My Everything''',background = '''http://www.hdbloggers.net/wp-content/uploads/2016/09/Field-of-Flowers-8.jpg`	''', text = '''It makes me happy just being by your side

	All these feelings I just cant hide

	You''ll always be in my heart

	Cant bear the pain when we are apart

	Nobody is as special as you are to me

	I hope you are beginning to see

	Just how much I care for you

	And all my feelings will always be true

	I can't describe how much I care

	But when you need me I'll be there

	To wipe those tears when you are sad

	To make you happy when you are mad

	All these things I can really do

	Just remember I'm thinking of you!!''', topic= '''romantic''')
	session.add(poemA1)
	session.commit()


if session.query(Poem).filter_by(name = '''You Mean The World To Me''' ).all() == []:	
	poemA2 = Poem(name='''You Mean The World To Me''', text = ''' You mean the world to me
	Nothing will ever come between us
	No matter what anybody says or does
	You will always be in my heart
	Forever and ever
	Your spot will never be replaced
	You hold the key to my heart
	And you have since we met
	I will love you forever
	And no matter how much we fight
	Things will be ok
	Like I said I will love you forever
	No matter what
	 ''', topic= '''romantic''')
	session.add(poemA2)
	session.commit()

if session.query(Poem).filter_by(name = '''My Promise To You''' ).all() == []:	
	poemA3 = Poem(name='''My Promise To You''', text = ''' I promise to always lift you up
When you are feeling down
I promise to wipe your tears
When you feel you need to cry
I promise to keep you smiling
To show off that beautiful smile you have
I promise to be your strength
Whenever you fall weak
I promise to be your voice,
When you can't find the words
I promise to be your eyes
When you cannot see
I promise to be your ears
When you cannot hear
I promise to always tell you what's real
When you want to hear the truth
I promise to be your dream catcher
To chase away you're every fear
I promise to be your smile
When you're frowning
I promise to always cheer you up
When you are down and blue
I promise to give you faith
When you are feeling insecure
I promise to keep you sturdy
When you are feeling unsafe
I promise to listen
When you need to talk
I promise to tell you no lies
Just what is true
I promise to always lend you my shoulder
For when you need to cry
I promise to always hold you
When you need someone
I promise to always care for you
Wherever you are I promise to always be there
I promise to never hurt you and never break your heart
I can't promise you the world
I can't promise you the sky
I can't promise you that we will never fight
I can't promise you that I will never cry
But I can promise you that I will always be true to you
And baby I promise that I will always love you more than anything with all my heart, no matter what happens or what we go through, baby I'll love you until the end of time!
Ill be your guardian angel
That's my promise to you!!

	 ''', topic= '''romantic''')
	session.add(poemA3)
	session.commit()

	session.commit()

	

	
if session.query(Poem).filter_by(name ='''TAHA''' ).all() == []:	
	poemA4= Poem(name='''TAHA''', text =''' TAHAA''', topic='''HAPPY''')
	session.add(poemA4)

session.commit()
