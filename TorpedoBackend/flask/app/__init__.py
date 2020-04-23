from flask import Flask , redirect ,url_for, flash, render_template



app = Flask (__name__)

from app import routes
