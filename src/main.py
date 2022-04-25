from flask import Flask, request
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
  print(request.environ)
  text = "<div>hello from flask</div>"
  text = text + "<div>request.remote_addr: %s</div>" % request.remote_addr
  return text + "<div>request.environ['REMOTE_ADDR']: %s</div><div>request.headers:<pre>%s</pre></div>" % (request.environ['REMOTE_ADDR'], request.headers)

if __name__ == '__main__':
  app.run(port=3000, debug=True)
