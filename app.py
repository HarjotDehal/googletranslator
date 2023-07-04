


# main application

from flask import Flask, render_template, request



from googletrans import Translator, LANGUAGES



# need to have all our
#  options and boxes in html. we send it the info from here in python. Simple. 



app = Flask(__name__)


# basically setting all our graphics first

# we gonna get our languages in an array qnd then send it over for our box

# we will have to probably
#  post or something after hitting the button or set something. 
# post/get may only be for tables tho. 


# langs = ['English','Hindi','Punjabi','German']
lang = list(LANGUAGES.values())
lang2 = list(LANGUAGES.values())

langs = lang

langs.remove('english')

langs.insert(0,'english')
translatesample =''





# use the Translator to convert
# def change(text="type", srcLang ="English", destlang ="Punjabi"):
#     text1 = text
#     srclangg= srcLang
#     destt=destlang
#     trans = Translator()
#     trans1 = trans.translate(text=text1,src=srclangg,dest=destt)
#     return trans1.text


# hardest part is getting our information from html to python
# we call this get translation from using our button. 
# we can have it send us to a new page but we still have to grab the data somehow. 
# def getTranslation():
#     # get the language which we want to translate from. from our html basically when we hit run. 
#     srclang = ""
# # get our dest lang
#     destlang = ""
# # our message to translate. use get (1.0,END) to get all of the data. 
#     masg = ""
#     ourtranslation = change(text=masg,srcLang=srclang,destlang=destlang)
#     # first delete everything in our destination message. 
#     # then set it again. we can get it with the .innerhtml
#     destinationText = ourtranslation

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == "POST":
        # get my data from request form. run it to my get translation
        # return it to rendertemplate with tag for translation
        sourceLanguage1 = request.form.get('leftlanguages')
        destinationlanguage1 = request.form.get('languagesright')
        mymessage = request.form['tobetranslated']
        # sourcelanguage = str(sourceLanguage1)
        # destinationlanguage = str(destinationlanguage1)

        # ourtranslation = change(text=mymessage,srcLang=sourceLanguage,destlang=destinationlanguage)
        # translatesample = ourtranslation
        try:
            trans = Translator()
            trans1 = trans.translate(mymessage,destinationlanguage1,sourceLanguage1)
        except:
            return f"<h1> You did not input all requirements. Go Back <h1/>"
        jatt = trans1.text
        leftlangss = lang
        leftlangss.remove(sourceLanguage1)
        leftlangss.insert(0,sourceLanguage1)

        rightlangss =lang2
        rightlangss.remove(destinationlanguage1)
        rightlangss.insert(0,destinationlanguage1)
        return render_template('index.html', leftlangs  = leftlangss,rightlangs =rightlangss, translated = jatt,totranslate =mymessage)
        # return jatt
    
    else:
        translatesample=''
        return  render_template('index.html', leftlangs  = langs,rightlangs =langs, translated = translatesample, totranslate=translatesample)



# if our request was a post, we already get our inputs which are the src lang, destlang
# and message. After our function, we return the render template
# with the final message attached so it fills like that. 



if __name__ =="__main__":
    app.run(debug=True)