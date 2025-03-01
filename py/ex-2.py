class hollow:
    has_hole_chest = True

class shinigami:
    has_zanpakto = True

class ichigo(hollow, shinigami):
    is_quincy = True

mc = ichigo()
print(mc.has_hole_chest, mc.has_zanpakto, mc.is_quincy)