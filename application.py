from main import application
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass
if __name__=="__main__":
    application.run(host="0.0.0.0",debug=True)
#app.run(debug=True)
