import pandas as pd
test_records =  [
                (1228, False, 1.0, 'QQ', 'VII', 'Pullover', 27.341917760765206, 617.516272605143, 2896.437068349862, 'AB', 0.00036614625001438027, 6.790803554896343e-05, False), 
                (1792, False, 1.0, 'AAT', 'X', 'Trouser', 92.06323912407882, 214.45262374753824, 2090.9883380607143, 'CP', 0.0006170868045364592, 0.00013976126468283044, False), 
                (1072, True, 1.0, 'WKN', 'VII', 'Bag', 53.559076271648806, 632.5399019492289, 1267.726492026083, 'HU', 0.04305724111608195, 0.00011397806633107171, False)]
test_formated_x = pd.DataFrame(
    {
        0:[1]+[0]*2,
        1:[0]*3,
        2:[0]*3,
        3:[0]*3,
        4:[0]*3,
        5:[0]*3,
        6:[0]*3,
        7:[0]*3,
        8:[0]*3,
        9:[0]*3,
    }
)

test_formated_y = pd.Series([False]*3)