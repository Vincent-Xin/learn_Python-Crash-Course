#8-9
magicians=['Jack','Tony','Tom']
def show_magicians(mags):
	for mag in mags:
		print(mag)
show_magicians(magicians)

#8-10
def make_great(mags):
	# new_mags=[]
	# while mags:
	# 	curr=mags.pop()
	# 	curr="the Great "+curr
	# 	new_mags.append(curr)
	# while new_mags:
	# 	mags.append(new_mags.pop())
	for i in range(0,len(mags)):
		mags[i]="the Great "+mags[i]
#8-11
	return mags

new_magicians=make_great(magicians[:])
show_magicians(new_magicians)
show_magicians(magicians)
