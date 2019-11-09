#9-10
import module

class IceCreamStand(module.Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors=['sugar','salt','ice']

	def show_kinds(self):
		for flavor in self.flavors:
			print(flavor)

ice_cream_store=IceCreamStand('icelove','kinds of icecream')
ice_cream_store.show_kinds()
ice_cream_store.set_number_served(12)

#9-11  
admin=module.Admin('Li','dashen','female','50')
admin.privileges.show_privileges()

#9-12
import module_2
admin_2=module_2.Admin_2('Li','dashen','female','50')
admin_2.privileges.show_privileges()
