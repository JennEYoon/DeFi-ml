## By Jennifer Yoon, March 2015, for R Programming class, Coursera.org.
## This function computes the inverse of a square, invertible matrix.
## Uses a cached solution to the inverse matrix, if one exists.
## Feel free to run it in RStudio using the test cases included at bottom.
## --------------------------------------------------------------------- ##

# Initialize global variables. Write to global inside function with "<<-".
mlist <- list()
slist <- list()

# Saves the original x matrix and its solved inverse matrix in a cache.
makeCacheMatrix <- function(x = matrix()) {
    i <- length(mlist) + 1
    mlist[[i]] <<- x
    slist[[i]] <<- solve(x)
}

# ----------------------------------------------------------------------- #
# Calculates the inverse matrix, but first checks for a cached solution.
cacheSolve <- function(x = matrix()) {
    # Check to see if x matrix already exists in cache (mlist).
    if (length(mlist) > 0) {
        for (i in 1:length(mlist)) {
            compare <- all(unlist(mlist[[i]]) == x)
            if (compare == T) {
                print("Using cached inverse.")
                return(slist[[i]])
            }
            # If match is found, return inverse from stored slist.
            # Note, slist ith matrix corresponds to mlist ith matrix.
            # Note R warns if dim of matrixes compared are not same.
        }    
    }
    # If no match in cache, call makeCacheMatrix(x) to make new cache.
    makeCacheMatrix(x)
    i = length(slist)
    return(slist[[i]])
    # Returns the last matrix in slist, which is the newly cashed solution.
}

# ----------------------------------------------------------------------- #
###########################################################################

#all(mlist[[2]] == mlist[[3]])
#m3 == all(mlist[[1]])
#all(m3 == unlist(mlist[[2]]))

# Test cases. 2 x 2 matix.
#m1 <- matrix(c(2,1,1,2), nrow=2, ncol=2)
#m2 <- matrix(c(2,1,2,2), nrow=2, ncol=2)
#m3 <- m2
#cacheSolve(m1)
#cacheSolve(m2)
#cacheSolve(m3)

# Test cases, 3 x 3 matrix.
m4 <- matrix(c(1,0,0,0,1,0,0,0,1), nrow=3, ncol=3)
m5 <- matrix(c(3,2,1,1,3,1,1,2,3), nrow=3, ncol=3)
m6 <- m4  # Repeats m4, should retrive answer from cache.
cacheSolve(m4)
cacheSolve(m5)
cacheSolve(m6)

# --------------------------------------------------------------#
