import web
import sqlite3

urls = (
       '/home', 'Home',
       '/action_page','Action'
       
       )

app = web.application(urls, globals())

render = web.template.render('templates/')

class Home(object):
    def GET(self):
        return render.Home()
        
class Action(object):
    
        
    def GET(self):
        conn = sqlite3.connect('STOCK.db')
        c = conn.cursor()

        c.execute("SELECT * from Exchange")
        conn.commit()
        t = ['SL NO.      CODE       NAME','-----      ------       -------']
        all_cols = c.fetchall()
        
        # Print the table contents
        
        for col in all_cols:
            
            t.append('{0}          {1}           {2}'.format(col[0], col[1], col[2]))
            
    
        return '\n'.join([ str(myelement) for myelement in t ])

        conn.close()

        
             
        
      
   
if __name__ == "__main__":
    app.run()
