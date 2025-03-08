import random
import string
import math
import datetime
import uuid
import os
import re

class RandomCode(object):
    def __init__(self):
        self.code = ''
    
    def generate_random_string(self, length=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
    
    def generate_random_integer(self, start=1, end=100):
        """Generate a random integer between start and end """
        return random.randint(start, end)
    
    def generate_uuid(self):
        """Generate a unique identifier"""
        return uuid.uuid4().hex
    
    def generate_random_datetime(self):
        """Generate a random datetime string in YYYY-MM-DDThh:mm:ssZ format """
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%dT%H:%M:%SZ")
    
    def generate_random_float(self, start=1.0, end=100.0):
        """Generate a random float between start and end """
        return round(random.uniform(start, end), 2)
    
    def generate_random_word(self, length=5):
        """Generate a random word of fixed length """
        words = ['apple', 'banana', 'orange', 'grape', 'pineapple']
        return random.choice(words)
    
    def generate_random_sentence(self, length=10):
        """Generate a random sentence of fixed length """
        sentence = ''
        for i in range(length):
            word = self.generate_random_word()
            if i == 0:
                sentence += word
            else:
                sentence += ' ' + word
        return sentence
    
    def generate_random_paragraph(self, length=20):
        """Generate a random paragraph of fixed length """
        paragraph = ''
        for i in range(length):
            sentence = self.generate_random_sentence()
            if i == 0:
                paragraph += sentence
            else:
                paragraph += ' ' + sentence
        return paragraph
    
    def generate_random_list(self, length=10):
        """Generate a random list of fixed length """
        lst = []
        for i in range(length):
            word = self.generate_random_word()
            lst.append(word)
        return lst
    
    def generate_random_dict(self, length=10):
        """Generate a random dictionary of fixed length """
        dct = {}
        for i in range(length):
            word = self.generate_random_word()
            dct[word] = word
        return dct
    
    def generate_random_tuple(self, length=10):
        """Generate a random tuple of fixed length """
        tup = ()
        for i in range(length):
            word = self.generate_random_word()
            tup += (word,)
        return tup
    
    def generate_random_set(self, length=10):
        """Generate a random set of fixed length """
        s = set()
        for i in range(length):
            word = self.generate_random_word()
            s.add(word)
        return s
    
    def generate_random_file(self, size=1024):
        """Generate a random file of fixed size """
        filename = 'test_' + str(uuid.uuid4()) + '.txt'
        with open(filename, 'wb') as f:
            for i in range(size):
                f.write(os.urandom(1))
        return filename
    
    def generate_random_email(self):
        """Generate a random email address"""
        local = self.generate_random_string() + '@'
        domain = self.generate_random_string() + '.' + self.generate_random_string()
        return local + domain
    
    def generate_random_url(self):
        """Generate a random URL"""
        protocol = random.choice(['http://', 'https://'])
        url = protocol + self.generate_random_string() + '.' + self.generate_random_string()
        for i in range(5):
            url += '/' + self.generate_random_string()
        return url
    
    def generate_random_ip(self):
        """Generate a random IP address"""
        octet1 = str(random.randint(0, 255))
        octet2 = str(random.randint(0, 255))
        octet3 = str(random.randint(0, 255))
        octet4 = str(random.randint(0, 255))
        return octet1 + '.' + octet2 + '.' + octet3 + '.' + octet4
    
    def generate_random_mac(self):
        """Generate a random MAC address"""
        mac = ''
        for i in range(6):
            mac += str(hex(random.randint(0, 255)))[2:]
            if i < 5:
                mac += ':'
        return mac
    
    def generate_random_guid(self):
        """Generate a random GUID"""
        return str(uuid.uuid4())
    
    def generate_random_datauri(self, mimetype='image/jpg', size=1024):
        """Generate a random data URI"""
        with open('test_' + str(uuid.uuid4()) + '.txt', 'wb') as f:
            for i in range(size):
                f.write(os.urandom(1))
        filename = 'test_' + str(uuid.uuid4()) + '.txt'
        with open(filename, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
        return 'data:' + mimetype + ';base64,' + b64