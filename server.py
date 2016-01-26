import tornado.web
import handlers
import motor

# Mongo DB
db = motor.MotorClient('localhost', 27017).mongoapi

# Setups the Main Server
def make_app():
    return tornado.web.Application([
        (r"/usercount", handlers.UserCountHandler),
        (r"/users", handlers.UsersHandler),
    ], db=db)

# Raises the main listener
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()