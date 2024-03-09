#include <iostream>
#include "BinaryTree.h"

int main()
{
    BinaryTree<char> tree(a);
    BinaryTree<int> tree;

    tree.insertR(20);
    tree.insertI(10);
    tree.insertR(30);
    tree.insertR(9);
    tree.insertI(15);
    tree.insertR(18);
    tree.insertR(7);
    tree.insertI(25);
    tree.insertI(7);
    tree.insertR(15);
    tree.insertR(14);

   std::cout << "\nMax data at level Iterative: ";
   tree.maxOfLevelI();
   std::cout << "\nMax data at level Recursive: ";
   tree.maxOfLevelR();

   std::cout << "\nLevels with the maximum count: ";
   tree.maxCountLevelI();

   std::cout << "tree constainsR 55: " << std::boolalpha << tree.containsR(55) << std::endl;
   std::cout << "tree constainsI 55: " << std::boolalpha << tree.containsI(55) << std::endl;
   std::cout << "tree constainsR 15: " << std::boolalpha << tree.containsR(15) << std::endl;
   std::cout << "tree constainsI 15: " << std::boolalpha << tree.containsI(15) << std::endl;
   std::cout << "tree constainsR -5: " << std::boolalpha << tree.containsR(-5) << std::endl;
   std::cout << "tree constainsI -5: " << std::boolalpha << tree.containsI(-5) << std::endl;

   std::cout <<"\npreorder recoursive: ";
   tree.preorderR();

    std::cout << "\npreorder iterative:  ";
    tree.preorderI();

   std::cout << "\ninorder recoursive: ";
   tree.inorderR();

    std::cout << "\ninorder iterative:  ";
    tree.inorderI();

   std::cout << "\npostorder recoursive: ";
   tree.postorderR();

   std::cout << "\npostorder iterative:  ";
   tree.postorderI();

   std::cout << "\nlevelorder iterative:  ";
   tree.levelorder();

   std::cout << "\nCount of Nodes: " << tree.countOfNodesR();
   std::cout << "\nCount of Leaves: " << tree.countOfLeavesR();

    std::cout << "\nHeight of Tree: " << tree.heightR();
    std::cout << "\nHeightPreorderI of Tree: " << tree.height_preorderI();
    std::cout << "\nheightLevelorderI of Tree: " << tree.height_levelorderI();
    std::cout << "\nWidth of Tree: " << tree.widthR();
    std::cout << "\nMax of Tree: " << tree.findMaxI();
    std::cout << "\nMin of Tree: " << tree.findMinR();
    
    std::cout << "deleting 7 15 20" << std::endl;

    tree.eraseR(7);
    tree.eraseR(15);
    tree.eraseR(20);
    tree.eraseR(15);


    std::cout << "\ninorder recoursive after deleting nodes: ";
    tree.inorderR();

    std::cout << "\nlevelorder iterative:  ";
    tree.levelorder();

    tree.clearR();

    std::cout << "\npostorder after clearing: ";
    tree.postorderR();

   std::cout << "\nMax data at level Iterative: ";
   tree.maxOfLevelI();
   std::cout << "\nMax data at level Recursive: ";
   tree.maxOfLevelR();

   std::cout << "\nLevels with the maximum count Iterative: ";
   tree.maxCountLevelI();
   std::cout << "\nLevels with the maximum count Recursive: ";
   tree.maxCountLevelR();

    std::cout << "\nTree is fullR: " << std::boolalpha << tree.isFullTreeR();
    std::cout << "\nTree is fullI: " << std::boolalpha << tree.isFullTreeI();


   BinaryTree<int> c = tree.copy();

   std::cout << "\npreorder iterative:  ";
   c.preorderI();

   std::cout << "\ninorder iterative:  ";
   c.inorderI();


    return 0;
}
