import System.IO

fuelNeeded :: Int -> Int
fuelNeeded m = (m `div` 3)-2

fuelNeededR :: Int -> Int
fuelNeededR m
    | calculatedFuel < 0 = 0
    | otherwise = calculatedFuel + fuelNeededR (calculatedFuel)
    where calculatedFuel = fuelNeeded m

main = do
    withFile "1dayinput" ReadMode (\handle -> do
            contents <- hGetContents handle
            print $ sum (map (\l -> fuelNeeded (read l)) (lines contents))
            print $ sum (map (\l -> fuelNeededR (read l)) (lines contents))
        )