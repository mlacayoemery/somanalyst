import re


if __name__=="__main__":
    exCodebook="3 hexa 1 1 gaussian\n# random seed: 0\n3.04401 5.6204 4.56623"
    naturalNumber="[0-9]+"
    somTopology="hexa|rect"
    neighborhoodType="gaussian"
    realNumber="-?[0-9]\.?[0-9]?"
    vector="(-?[0-9]\.?[0-9]?){1}( -?[0-9]\.?[0-9]?){2}"

    tester=vector
    test="-0.0 -0.0 -0.0"
    p=re.compile(tester)
    print
    print p.match(test).group(0)