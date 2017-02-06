from databases import *
engine = create_engine('sqlite:///poems.db')
Base.metadata.bind= engine
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()



### Initialize database with entries ###
if session.query(Poem).filter_by(name = '''You're My Everything''' ).all() == []:
	poemA1 = Poem(name='''You're My Everything''', text = '''It makes me happy just being by your side

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
	















#poem1B = Poem(name = "poem1B" , text = "t123445565656", topic= 'romantic')
#quote1A =Quote( text = "text of quote", topic = 'happy')
#quote1B =Quote(text = "ITS A LOVE ", topic= 'romantic')
#poem11= Poem(name = "poem11" , text = "t123445565656", topic= 'political')
session.commit()
