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
        return render.home()
    
        
    def POST(self):
    
        form = web.input(name="market")
        
        conn = sqlite3.connect('STOCK.db')
        c = conn.cursor()
        
        

        c.execute("SELECT * from Exchange")
        conn.commit()
        t = ['SL NO.      CODE       NAME','-----      ------       -------']
        all_cols = c.fetchall()
        for col in all_cols:
            
            t.append('{0}          {1}           {2}'.format(col[0], col[1], col[2]))
            
        c.execute("SELECT * from Company")
        conn.commit()
        t1 = ['SL NO.      NAME       CODE','-----        ------         -------']
        all_cols1 = c.fetchall()
        for col1 in all_cols1:
            
            t1.append('{0}          {1}           {2}'.format(col1[0], col1[1], col1[2]))
            
        c.execute("SELECT * from Stock")
        conn.commit()
        t2 = ['SL NO.      SYMBOL       COMPANYid        EXCHANGEid','-----        ------         -------      -------']
        all_cols2 = c.fetchall()
        for col2 in all_cols2:
            
            t2.append('{0}          {1}           {2}            {3}'.format(col2[0], col2[1], col2[2], col2[3]))     
        conn.close()       
            
        if form.market == "Exchange" :
            return '\n'.join([ str(myelement) for myelement in t ])
            
        elif form.market == "Company" :
            return '\n'.join([ str(myelement) for myelement in t1 ])
            
        elif form.market == "Stock" :
            return '\n'.join([ str(myelement) for myelement in t2 ])                
      
   
if __name__ == "__main__":
    app.run()
