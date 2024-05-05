# from bottle import default_app, get, post, run
# import git

from bottle import default_app, get, post, run, response, Bottle
import git, json
 
app = Bottle()
 
@post('/secret_url_for_git_hook')
def git_update():
  repo = git.Repo('./uw_exam')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""
 
 
##############################
@get("/")
def _():
  return "Your connection is successful! :)"
 
##############################

@get("/crimes")
def _():
    try:
        # Assuming your JSON file is named data.json
        with open("/home/mari78f9/ultimate-web/crime.json", "r") as f:
            data = json.load(f)
        response.content_type = 'application/json'
        return json.dumps(data)
    except Exception as e:
        return f"Error: {e}"
 
if __name__ == "__main__":
    run(app, host='0.0.0.0', port=8080, debug=True)

##############################
try:
  import production
  application = default_app()
except Exception as ex:
  print("Running local server")
  run(host="127.0.0.1", port=80, debug=True, reloader=True)