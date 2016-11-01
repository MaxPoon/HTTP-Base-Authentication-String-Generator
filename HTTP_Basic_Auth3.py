import hashlib
import hmac
import struct
import time
import base64

def hotp(secret, counter, digits=10, alg=hashlib.sha1):
	c = struct.pack('>Q', counter)
	b = bytearray()
	b.extend(map(ord,secret))
	secret=b
	hash = hmac.new(secret, c, alg).digest()
	offset = hash[-1] & 0x0F
	result = hash[offset:offset+4]
	result = struct.unpack('>L', result)[0] & 0x7FFFFFFF
	result = result % 10 ** digits
	return '%0*d' % (digits, result)

def totp_counter(t=time.time(), t0=0, timestep=30):
	return int((t - t0) / timestep)

def totp(secret, t0=0, timestep=30, digits=10, alg=hashlib.sha1):
	t = time.time()
	return hotp(secret, totp_counter(t, t0, timestep), digits, alg)

def HTTP_Basic_string (user_id, secret, t0=0, timestep=30, password_digits=10, alg=hashlib.sha1):
	password = totp(secret,t0,timestep,password_digits,alg)
	plaintext = user_id+':'+password
	ciphertext = base64.b64encode(bytes(plaintext,'utf-8'))
	result = "Basic "+ciphertext.decode('utf-8')
	return result
