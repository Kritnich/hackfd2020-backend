# Placeholder file for an implementation that lets us verify
# infection codes given by the German public health authority
# We have no API with them obviously, so this just returns true.

def verify_infection(code):
    if code == 'iminfected':
        return True
    else:
        return False
