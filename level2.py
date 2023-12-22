def solution(h, q):
    # Your code here
    # Find parent
    def parent(a,h):
        '''
        If root = 2^h - 1
            Left subtree in range(1,2^(h-1))
            Right subtree in range(2^(h-1),root)
        '''
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
    
    '''
    solution(5, [19, 14, 28])  # Expected output: [21, 15, 29]
    solution(3, [7, 3, 5, 1])  # Expected output: [-1, 7, 6, 3]
    '''
    
    return converter