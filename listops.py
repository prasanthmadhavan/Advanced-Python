
def first(a):
	return a[0]

def rest(a):
	return a[1:]

def last(a):
	return a[-1]

def null(a):
	return len(a) == 0

def cons(item, a):
	return [item] + a

def element(a,b):
	if null(a): return
	elif first(a)==b: return first(a)
	else: return element(rest(a),b)

def append(a,b):
	if null(b): return a
	elif null(a): return b
	else: return cons(first(a),append(rest(a),b))

def reverse(a):
	if null(a): return []
	else: return append(reverse(rest(a)),[first(a)])

def inter(a,b):
	if null(a): return []
	elif null(b): return []
	elif (first(a)) in b:
		return cons(first(a),inter(rest(a),b))
	else: return inter(rest(a),b)

def flatten(a):
        if null(a):
                return []
        elif type(first(a))==list:
                return append([first(first(a))],flatten(rest(first(a)+rest(a))))
        else: return append([first(a)],flatten(rest(a)))


def max(a):
	if null(a): return []
	if rest(a)==[]: return a
	elif last(a)>first(a): return max(rest(a))
	else : return max(rest(reverse(a)))
