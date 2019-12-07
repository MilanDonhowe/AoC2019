{- Advent of Code Day 6 -}

import System.IO
import Data.List.Split

data Tree a = Root (Tree a) | EmptyNode | Leaf a (Tree a) (Tree a) deriving (Show, Eq)

treePushNode :: Tree a -> Tree a -> Tree a
treePushNode newLeaf (Root oldTree) =

parseToTree :: [String] -> Tree String
parseToTree orbitData = (map(\x -> x).splitOn(")").head) (orbitData)

{-
D)C
C)E
COM)D
-}