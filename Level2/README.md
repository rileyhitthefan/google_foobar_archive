# Ion Flux Relabelling 

## Problem Summary
> Oh no! Commander Lambda's latest experiment to improve the efficiency of her LAMBCHOP doomsday device has backfired spectacularly. She had been improving the structure of the ion flux converter tree, but something went terribly wrong and the flux chains exploded. Some of the ion flux converters survived the explosion intact, but others had their position labels blasted off. She's having her henchmen rebuild the ion flux converter tree by hand, but you think you can do it much more quickly - quickly enough, perhaps, to earn a promotion!
>
> Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one. To label them, she performed a post-order traversal of the tree of converters and labeled each converter with the order of that converter in the traversal, starting at 1. For example, a tree of 7 converters would look like the following:
```
      7
    /   \
  3      6
 /  \   / \
1   2  4   5
```
> Write a function answer(h, q) - where h is the height of the perfect tree of converters and q is a list of positive integers representing different flux converters - which returns a list of integers p where each element in p is the label of the converter that sits on top of the respective converter in q, or -1 if there is no such converter. For example, answer(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4, and 7 in a perfect binary tree of height 3, which is [3, 6, -1].
>
> The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root, h = 2 represents a perfect binary tree with the root and two leaf nodes, h = 3 represents a perfect binary tree with the root, two internal nodes and four leaf nodes (like the example above), and so forth. The lists q and p contain at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.

## Approach (Python)
Find the parent node by using recursive function to reduce the child node and height to base case (child, height) or (a, h) equals:
- or (root, log<sub>2</sub>(root))
- or (left/right child of root, log<sub>2</sub>(root))

Some useful properties:
- root = 2<sup>h</sup> - 1
- left child of root = 2<sup>h-1</sup> - 1 --> Range of left subtree is range(1, 2<sup>h-1</sup>)
- right child of root = root - 1 --> Range of right subtree is range(2<sup>h-1</sup>, root)

Looking at the 2 ranges, 2<sup>h-1</sup> can be used as a comparison to figure out whether the child is a left or right child. If left, keep the child and reduce the height by 1. If right, reduce the child by its root's left child value and reduce the height by 1, then readd the subtracted value. Do this recursively until base case.

![Revised notes and calculations](https://scontent.fyzd1-3.fna.fbcdn.net/v/t1.15752-9/409965580_895946478902461_605955524987797450_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=Gcvk1KobEbkAX-oidr5&_nc_ht=scontent.fyzd1-3.fna&oh=03_AdSsRwy9uPvSSfOTYtaLj9xajXWem7FfLOXDB91U2CbKzw&oe=65AD1950)

## Solution (Python)
```
def level2(h, q):
      # Find parent
      def parent(a,h):
            # If root = 2^h - 1
            # Left subtree in range(1,2^(h-1))
            # Right subtree in range(2^(h-1),root)
            root = 2**h - 1
            mid = 2**(h-1) 
            # If root 
            if a == root:
                  return -1
            # If child of root
            if a==mid-1 or a==root-1:
                  return root

            # Other descendants
            if a>=mid:
                  return parent(a-(mid-1),h-1) + mid - 1
                  return parent(a,h-1)

      # Convert
      converter = []
      for i in q:
            convert = parent(i, h) 
            converter.append(convert)

      return converter
```
