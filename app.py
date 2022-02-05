from waitress import serve
from urllib.parse import parse_qsl
from re import sub,IGNORECASE
from roman import toRoman

def app(environ, start_response):
  def render(data, error_code):
    if error_code == 200:
      status = "200 OK"
    elif error_code == 404:
      status = "404 Not Found"
    else:
      status = "500 Internal Server Error"
  
    try:
      data = data.encode()
    except BaseException:
      status = "500 Internal Server Error"
      data = b"Could not encode data"
  
    start_response(status, [
      ("Content-Type", "text/plain"),
      ("Content-Length", str(len(data)))
    ])
    return iter([data])

  data = ''
  print(environ)
  if 'PATH_INFO' in environ and environ['PATH_INFO']=='/az' and 'QUERY_STRING' in environ:
    try:
      params = dict(parse_qsl(environ['QUERY_STRING']))
      if 'game' not in params:
        data = 'UnknownGame'
        return render(data, 404)
      game_name = str(params['game']).strip()
      data = game_name
      try:
        game_name = sub(r'^the\s', '', game_name, flags=IGNORECASE)
        game_name = sub(r'[^a-zA-Z0-9]+', '', game_name)
        game_name = sub(r'(\d+)', lambda m: toRoman(int(m.group(1))), game_name)
        game_name = sub(r'legendofzelda', 'TLOZ', game_name, flags=IGNORECASE)
        game_name = sub(r'ocarinaoftime', 'OoT', game_name, flags=IGNORECASE)
        data = game_name
      except BaseException as err:
        try:
          data = sub(r'[^a-zA-Z0-9]+', '', game_name)
        except BaseException:
          pass
        print(f"""Error while parsing game name {err=}, {type(err)=}""")
      data = data[0:13]
      if not game_name or not data:
        data = 'UnknownGame'
        return render(data, 404)
      return render(data, 200)
    except BaseException as err:
      data = f"""Error while parsing game name {err=}, {type(err)=}"""
      return render(data, 500)
  else:
    return render('Missing game, or unknown path', 404)
#serve(app, listen='*:8080')
