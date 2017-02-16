from databases import *
engine = create_engine('sqlite:///poems.db')
Base.metadata.bind= engine
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()



### Initialize database with entries ###
quote1=Quote(text= ''' i am in love ''',topic = '''romantic''')
session.add(quote1)
session.commit()
if session.query(Poem).filter_by(name = '''You're My Everything''' ).all() == []:
    poemA1 = Poem(name='''You're My Everything''',background = '''http://www.hdbloggers.net/wp-content/uploads/2016/09/Field-of-Flowers-8.jpg`  ''', text = '''It makes me happy just being by your side

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
     ''', background= "https://cdn.pixabay.com/photo/2015/06/17/17/20/rose-812765_1280.jpg" , topic= '''romantic''')
    session.add(poemA2)
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
     ''', background= "https://cdn.pixabay.com/photo/2015/06/17/17/20/rose-812765_1280.jpg" , topic= '''romantic''')
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

     ''', background = "http://4.bp.blogspot.com/-TvMlyPzGQxs/VqCmDCI-jHI/AAAAAAAABLg/deSosVJdG7g/s1600/Romantic-Status-in-English-for-WhatsApp-%2526-Facebook-02.jpg", topic= '''romantic''')
    session.add(poemA3)
    session.commit()
if session.query(Poem).filter_by(name = '''Life Moves Way Too Fast''' ).all() == []:    
    poem10 = Poem(name='''Life Moves Way Too Fast''', text = ''' You're the reason I get up to face each hectic day
How did our lives get so consumed with nonsense on the way
We used to take the time to laugh and play a game or two
But now it seems we fight a lot and cry way too much too
So when you go to sleep at night I'll slip in by your side
I'll hold you close and squeeze you tight and feel amazing pride
You're the one that I love best, it's very clear to see
With every day I know I'm blessed that you're a part of me
Now let's just try to slow it down and savor all that's past
For that's what molds our future, and life moves way too fast

     ''', topic= '''romantic''')
    session.add(poem10)
    session.commit()


if session.query(Poem).filter_by(name = '''Love At First Sight''' ).all() == []:    
    poem11 = Poem(name='''Love At First Sight''', text = ''' When first we touched,
My heart flew high,
On gossamer wings through a cloudless sky.
They said it was built upon a lie.
They told me my feelings would surely fade.
Passion would flare and foes would be made.
Can you not put the pass behind?
True love can change a rivers course,
Or pierce the strongest vault with ease.
True love can turn coal into gold,
Or tame the tempest to a balmy breeze.
Quite some time has passed since then:
People no longer criticize,
For now they see that truth exists,
Where once there might have been only lies.
Still my feelings are the same today,
As they were on that very first,
For when we touch, my heart still flies, on gossamer wings through cloudless skies.

     ''', topic= '''romantic''')
    session.add(poem11)
    session.commit()
    

if session.query(Poem).filter_by(name = '''My Sanctuary''' ).all() == []:   
    poem13 = Poem(name='''My Sanctuary''', text = ''' In your arms

Time stops for a brief moment

We're in our own world

Worries or thoughts

Completely gone


Focused on each other

Speaking briefly


Or in peaceful silence

We enjoy each other's presence

I take in the way you smell

Masculine with a hint of sensitivity thrown in

Holding your hand

Studying your long, slender fingers

Your hand as a whole

Strong, yet gentle


Memorizing every detail of your face
Your long lashes

Covering your blue-grey eyes
With flecks of green
Your aquiline nose
That balances your long lean face
Just right


     ''', topic= '''romantic''')
    session.add(poem13)
    session.commit()
    

if session.query(Poem).filter_by(name = '''Big Brother Gone''' ).all() == []:   
    poem14 = Poem(name='''Big Brother Gone''', text = '''Day by day I think of you,
How can all of this be true?
I can't believe you're really gone,
I still can't accept it,
Even after so long.
Just the thought of you makes me cry,
I never even got the chance to say goodbye.
Every picture, every letter,
I don't know if it will ever get better.
I always smell your familiar scent,
It makes me think of all of the times we've spent.
I know we didn't always get along,
And every time we talked, it would always go wrong.
So many things I never got to say,
I never imagined you'd ever be so far away.
You were my brother,
And I loved you like no other.
In my heart you'll always be,
You'll be my guide and help me see.
I'll never forget your soothing voice,
I would take your place if I had a choice.
But now I have to let you rest,
Although without you my world's a mess.
I miss you with all of my heart,
I wish we never had to part.
I know you're always by my side,
So now I guess this is my goodbye... 
     ''', topic= '''sad''')
    session.add(poem14)
    session.commit()        

if session.query(Poem).filter_by(name = '''In Our Hearts''' ).all() == []:  
    poem15 = Poem(name='''In Our Hearts''', text = '''

We thought of you with love today,
But that is nothing new.
We thought about you yesterday
And days before that, too.
We think of you in silence.
We often speak your name.
Now all we have is memories
And your picture in a frame.
Your memory is our keepsake
With which we'll never part.
God has you in his keeping.
We have you in our heart.
-loosing-a-father 
     ''', topic= '''sad''')
    session.add(poem15)
    session.commit()        

if session.query(Poem).filter_by(name = '''My Aunt Jean''' ).all() == []:   
    poem15 = Poem(name='''My Aunt Jean''', text = ''' I close my eyes as I wipe a tear.
I just keep wishing you were still here.
I will hold all the memories deep in my heart.
Through these memories will never part.

I close my eyes as I wipe a tear.
I just keep wishing this pain would disappear.
I didn't get the chance to say my last good-bye.
I just didn't think you could ever die.

I close my eyes as I wipe a tear.
All of your love I will always hold near.
In my heart and my mind I will never be alone.
When my time comes......
I will meet you in heaven!
WE LOVE AND MISS YOU!

     ''', topic= '''sad''')
    session.add(poem15)
    session.commit()        
                
if session.query(Poem).filter_by(name = '''Loved Ones''' ).all() == []: 
    poem16 = Poem(name='''Loved Ones''', text = ''' Loved ones are precious
I know this for a fact
And when you lose one
It's like an attack

I've lost some loved ones
To many different things
I hate losing loved ones
But it's a bell that has to ring

Loved ones are special
I have many I should know
But it just seems
I couldn't let them go

You try so hard
To hold on
But in one small second
Loved ones are gone

Sometimes at night
I pray for lost loved ones
Even though they won't come back
This poem is for them the loved ones

Lloyd Nadine
Rhonda Trish
And Ashley
I love you all

     ''', topic= '''sad''')
    session.add(poem16)
    session.commit()        
                
if session.query(Poem).filter_by(name = '''God Can You Hear Me?''' ).all() == []:   
    poem17 = Poem(name='''God Can You Hear Me?''', text = '''My eyes fill with tears,
And I could hardly see.
This cancer is stealing my father,
Slowly away from me.

I can't stand to see him suffer,
I pray his pain would go away.
His light inside him fades a little more
With every passing day.

Please give him the courage
To fight a little longer
I feel so helpless now
What can I do to help make him stronger?

I can see it in his eyes
It's like he wants to give in
Cancer CAN be fought
But you have to WANNA win

Can't he see that we need him
Shouldn't that be enough
He has to think positive
I know my dad is tough.

I sit and think and think
Until my head wants to explode
Always the same question: why him?
But the answer is still untold.

I wish by some miracle
His cancer would just disappear
And I could have my father back
And there would be no more fear

God can you hear me?
I never ask for much
Would it be so wrong for me to ask
That you give my dad your special touch?

I'm not asking for money
Or diamonds or even a pearl
I'm simply asking you to help him fight
Signed: daddy's little girl!

Source: http://www.familyfriendpoems.com/poem/god-can-you-hear-me 
     ''', topic= '''sad''')
    session.add(poem17)
    session.commit()        
                
if session.query(Poem).filter_by(name = '''Depression Is Never Ending''' ).all() == []: 
    poem18 = Poem(name='''Depression Is Never Ending''', text = ''' Depression is here every day,
And it never goes away.
Go away! I yell into the dark,
As if someone is there.
I feel as if I'm a prisoner
In the dungeon's lair.
And as always, no one cares.
Do I dare?
Dare to care about anyone but me?
Could it be,
Someone there?
Someone there to care?
No, just an image.
That's the way it will always be,
No matter how hard I try.
I just want to get by.
I go through life day by day.
I thought pain was supposed
To go away with time,
But it's not.
It's still here,
Here with the fear,
Fear that I will get hurt more.

     ''', topic= '''sad''')
    session.add(poem18)
    session.commit()        
                
if session.query(Poem).filter_by(name = '''My Fears''' ).all() == []:   
    poem19 = Poem(name='''My Fears''', text = '''Getting left behind
Not being loved
No one understanding
No one caring
are
my fears

I had a dream
I was lost
No one tried to
find me
No one cared
No one listened
understood

Feeling left out
Feeling like no one
understands
Feeling like no one
can hear me
When I'm screaming
to be heard
Destructive behavior
I have

Wishing I could change
Wishing I could make it
better
Wishing for another chance
Wishing for someone who
will come and save me
from myself.

my fears
not being heard
being left behind
not being understood
no one caring.

how can I
disappear
make people
understand.

Disappear from
this world
Show people what
It's like to
worry, misunderstand
not care.

my fears,
people laugh
people tease
people misjudge
people misunderstand
me.
Behind my back,
they laugh,
tease,
hurt,
so I can't see
them. It hurts.

Now,
I hide this
pain
in my heart
making sure
No one sees
my hurt,
Pretending to be
someone
I'm not.

Trying so hard
to fit in
to cover the
scars, trying
so hard,
to be liked
by you.

My feelings
disappearing
No regrets
Hoping no one
resents me.

After my dream
ended
I wondered...
What am I leaving..
When I leave here?

The pain
I've caused the hurt
the disappointments
The worries

Hoping, now
people understand
people miss
people hear me
and others
Forgetting all,
all the pain, and hurt
I learned to hide
inside
buried deep in
my heart. No way
out

My fears...are these..

     ''', topic= '''sad''')
    session.add(poem19)
    session.commit()        

if session.query(Poem).filter_by(name = '''How Could I Be So Lonely''' ).all() == []:   
    poem20 = Poem(name='''How Could I Be So Lonely''', text = ''' How could I be so lost,
In a place I know so well?
How could I be so broken,
In a family so together?
How could I be so lonely,
Surrounded by so many?
How could I be so unhappy,
Surrounded by so much beauty?
How could I be me,
When even I remain a mystery?

     ''', topic= '''sad''')
    session.add(poem20) 
    session.commit()        

if session.query(Poem).filter_by(name = '''Waiting For My Dad''' ).all() == []: 
    poem21 = Poem(name='''Waiting For My Dad''', text = '''I sit alone in the darkness
Waiting...
Waiting for him to come back to me.
Can he hear my cries?
Can he feel my tears?
Can he sense my breaking heart?
God only knows such a fact.
How can this be that he can't see me?
Is it because I'm sitting alone in the darkness?
I just walk past everyone as if I were invisible.
Can he see me now?
Can he see the pain he's caused me?
Or does he look past it?
I think I should move on,
But something tells me to wait.
It's my heart.
I'll give him one more chance
He needs to prove his love to me.
As I return to sit alone in the darkness...
Waiting.

     ''', topic= '''sad''')

    session.add(poem21)
    session.commit()        

if session.query(Poem).filter_by(name = '''All I Want''' ).all() == []: 
    poem22 = Poem(name='''All I Want''', text = '''

My life sucks so bad, and
no one knows.
I can't stand to take it anymore.
I want to leave so bad and she won't let me.

I want to run but my legs won't move.
I want to scream but my voice is silenced by her.
I want to cry but my eyes are dry.
I want to die but no one will let me go.

All I want to do is not be me!
My life is so messed up and no one knows.
Will they ever?



     ''', topic= '''sad''')
    session.add(poem22)
    session.commit()        

if session.query(Poem).filter_by(name = '''Without You''' ).all() == []:    
    poem23 = Poem(name='''Without You''', text = ''' I HATE being patient, but I've got more of it than anyone else I know
I HATE having to put my self aside for something else,
but I care enough to do it
I find myself filled with a lot of that lately... this... Hate...
It sounds so weird to say it out loud... Hate.... It doesn't have a nice feeling.
I HATE-
It's just not me.
It's not how I want to be.
It doesn't sound right coming out of my mouth.
It doesn't sound right swirling through my head
why is it that I find myself constantly forcing that word out of my head.
I hate that...
there it is again,
lately It creeps up on me.
I know what causes it. I'm tired.
I'm tired of being patient and putting myself second
second for you
I hate you
I don't hate you.
I hate the power you seem to have over me
I hate that I can't hate you.
I feel helpless,
The words echo through my head. They echo through the room.
The room
This room.
I hate this room.
The room you so kindly took the time to build for me.
the room in my head.
once my sanctuary. - now my enemy.
I hate this room.
I'm forced to sit in this damp windowless room.
there is no way out. Not yet anyways.
I have to wait.
wait - And be patient.
wait...
for you.

     ''', topic= '''sad''')
    session.add(poem23)
    session.commit()        

if session.query(Poem).filter_by(name = '''Good Mommy''' ).all() == []: 
    poem24 = Poem(name='''Good Mommy''', text = ''' You can't prepare for this:
the DNR in red letters,
last rites over,
the monitors off,
the harsh fluorescent lights,
the curtains drawn,
and the bed rail down
because there is no place left
for your mother to fall.

And then you see her,
one eye half open,
her hands clawed like eagle talons,
her dry lips form an O of surprise,
and the tangled blue diamonds
of her hospital gown.

You reach for her,
bury your face
in the wing of her collarbone,
caress her cool cheeks,
then run your hands
down the rough cotton blanket,
feel how small she is.

Your chest is tight and aches;
this is what heart break
feels like, and now
you know.

You hear a rustle,
a young nurse presses
tissues and a phone
into your shaking hands,
ring ring ring ring,
but it's rush hour
and no one's home, yet.

You sit down so the nurse
can close your mother's eyes
and fold her hands on her chest,
while you stare at the table,
her dentures, her silver eyeglasses,
and the thick novel you brought
because she was supposed to live
through this night,
and the next.

You have some time
to straighten her matted wig,
brush some pink blush
on her waxy cheeks,
rub vanilla gloss
on her chapped lips,
spray her wrists
with sweet lavender cologne.

You remember
how much she liked cheap beer,
long cigarettes, and television,
how she knit you a white sweater
with three black kittens
for the first day of school,
how she got drunk one night
and called you a tramp.

You regret telling her
to go straight to hell,
because you know
she had a hard time
raising three kids alone,
Besides, fourteen years
of bone cancer
was hell enough.

You drag your chair to the bed,
wipe the hot tears from your face,
rub her stick thin legs,
and whisper,
'You were a good mommy,'
the same words
you will write on a slip of paper
and tuck behind the crepe pillow,
just before they close her casket.


     ''', topic= '''sad''')
    session.add(poem24)
    session.commit()        

if session.query(Poem).filter_by(name = '''Time To Let Go''' ).all() == []: 
    poem25 = Poem(name='''Time To Let Go''', text = '''Today I sat and tried my best to think.
If it could end your life why would you drink?
I wish I knew how to change your mind.
Life is too precious to leave it all behind.
How can you just turn around and walk away.
When we need a dad here for us today.
Is that what you want the easy way out?
To leave this world without any doubt.
So stop a minute and take a deep breath.
Drinking like this could lead to your death.
Think of everything you have before you choose.
If you don't stop drinking that is what you will lose.
After all these years there is one thing I now know.
If I love you this much it time to let go

     ''', topic= '''sad''')
    session.add(poem25)                 
    session.commit()        

if session.query(Poem).filter_by(name = '''Darkness''' ).all() == []:   
    poem26 = Poem(name='''Darkness''', text = ''' Its like a plague that never goes away,
Or an animal and its prey,
It waits...
And waits...
And waits...until you're ready,
Then closes in and devours you...
From the inside out.
ALL you see is shadows of the ones you once knew,
No more happiness,
No more laughter,
No more love,
Its like a thunderstorm that blocks your soul.
Your soul becomes a black hole,
Whatever said, heard, or learned,
Is forgotten, never brought up again,
No longer does anything matter,
Its all darkness,
Like a plague that never goes away.
     ''', topic= '''sad''')
    session.add(poem26)
    session.commit()        

if session.query(Poem).filter_by(name = '''Cold Dark Corner''' ).all() == []:   
    poem27 = Poem(name='''Cold Dark Corner''', text = ''' There's a cold dark corner
in the back of my room,
it speaks to me
and says I'm coming for you.

As I lie on my bed
in the fetal position,
my eyes are closed
hoping and wishing.

Maybe that one day
my dreams will come true,
that I don't have to be here
so down and blue.

The corner keeps talking
about how I'm going to die,
all I can do
is lie there and cry.

As the corner gets closer
and takes me in,
my soul starts to burn
as so does my skin.

My bones shall lie there
turning to dust,
my bed surrounding
nothing but rust.

     ''', topic= '''sad''')
    session.add(poem27)
    session.commit()    
    session.commit()

    

 


if session.query(Poem).filter_by(name ='''How Could I Be So Lonely''' ).all() == []:    
    poemA5= Poem(name='''How Could I Be So Lonely''', text =''' How could I be so lost,
In a place I know so well?
How could I be so broken,
In a family so together?
How could I be so lonely,
Surrounded by so many?
How could I be so unhappy,
Surrounded by so much beauty?
How could I be me,
When even I remain a mystery?''', background="http://mediad.publicbroadcasting.net/p/kera/files/styles/medium/public/201509/lonly_0.jpg", topic='''Sad''')
    session.add(poemA5)

    session.commit()

