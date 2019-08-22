from unittest import TestCase
import unittest

# inital simple solution which solves the problem (takes just over 5 seconds for the extremely large list)
def largest_loss_brute(pricesLst):
    l = 0
    for i in range(len(pricesLst) - 1, 0, -1):
        for j in range(0, i):
            if (pricesLst[i] - pricesLst[j] > l):
                l = pricesLst[i] - pricesLst[j]
    return l


# after spending some more time thinking, I came up with a much better algorithm. This solves the extremely large list task in less than 0.1 seconds.
def largest_loss(pricesLst):
    if len(pricesLst) < 2:
        return 0

    left = pricesLst[0]
    right = 100000
    loss = -100000
    pot_right = 100000
    
    for i in range(1, len(pricesLst)):
        c = pricesLst[i]

        if ((c - min(left, right)) > loss):
            left = min(left, right)
            right = c
            loss = right - left
        
        if (c - pot_right > loss):
            left = pot_right
            right = c
            loss = right - left

        if (c < min(left, right, pot_right)):
            pot_right = c

            
    return loss
            
            
        
    
    
class TestLargestLoss(TestCase):
    
    def test_largest_loss_normal(self):
        loss = largest_loss([1, 2, 3, 4, 5])
        self.assertEqual(loss, 4)
        loss = largest_loss([1, 3, 5])
        self.assertEqual(loss, 4)
        loss = largest_loss([2, 4])
        self.assertEqual(loss, 2)

    def test_largest_loss_random(self):
        loss = largest_loss([5, 1, 3, 7, 9])
        self.assertEqual(loss, 8)
        loss = largest_loss([3, 4, 7, 9, 3, 5])
        self.assertEqual(loss, 6)

    def test_largest_loss_one_elem(self):
        loss = largest_loss([5])
        self.assertEqual(loss, 0)

    def test_largest_loss_two_elems(self):
        loss = largest_loss([5, 9])
        self.assertEqual(loss, 4)

    def test_largest_loss_smallest_first(self):
        loss = largest_loss([1, 3, 7, 4, 9])
        self.assertEqual(loss, 8)

    def test_largest_loss_smallest_middle(self):
        loss = largest_loss([5, 1, 1, 7, 9])
        self.assertEqual(loss, 8)

    def test_largest_loss_smallest_last(self):
        loss = largest_loss([5, 3, 7, 9, 1])
        self.assertEqual(loss, 6)

    def test_largest_loss_all_same(self):
        loss = largest_loss([5, 5, 5, 5, 5])
        self.assertEqual(loss, 0)

    def test_largest_loss_very_large_list(self):
        huge_list = [783, 174, 670, 315, 801, 425, 329, 886, 787, 454, 803, 746, 539, 440, 265, 450, 863, 557, 819, 160, 428, 145, 618, 54, 232, 908, 82, 541,
                 751, 886, 144, 459, 737, 433, 980, 704, 859, 643, 908, 496, 659, 750, 557, 649, 997, 454, 998, 400, 956, 999, 917, 563, 74, 65, 992, 250,
                 719, 350, 487, 927, 400, 306, 318, 805, 330, 812, 43, 590, 582, 771, 506, 946, 345, 10, 923, 119, 776, 748, 770, 798, 545, 198, 167, 571,
                 537, 875, 156, 655, 68, 833, 761, 883, 61, 435, 584, 664, 548, 50, 857, 339, 637, 967, 607, 109, 600, 229, 694, 635, 755, 682, 4, 801, 152,
                 442, 738, 388, 196, 571, 957, 718, 867, 351, 176, 942, 935, 739, 28, 699, 674, 594, 408, 919, 446, 830, 526, 607, 651, 493, 443, 277, 297,
                 670, 683, 203, 110, 317, 389, 408, 70, 875, 102, 829, 750, 782, 508, 368, 651, 185, 27, 975, 306, 673, 872, 273, 403, 41, 141, 203, 789,
                 124, 598, 319, 990, 223, 108, 592, 56, 123, 337, 474, 705, 949, 104, 14, 264, 524, 959, 885, 663, 239, 998, 746, 472, 766, 195, 277, 113,
                 714, 578, 312, 837, 433, 941, 158, 91, 460, 27, 940, 227, 531, 562, 626, 88, 709, 315, 884, 856, 410, 439, 13, 744, 686, 473, 451, 126,
                 178, 254, 978, 593, 7, 540, 642, 490, 465, 82, 656, 709, 222, 908, 935, 953, 806, 568, 771, 236, 702, 482, 761, 753, 720, 387, 396, 201,
                 564, 477, 168, 151, 865, 774, 801, 123, 544, 142, 260, 610, 863, 394, 237, 381, 486, 374, 384, 62, 198, 727, 753, 739, 65, 919, 492, 733,
                 92, 59, 715, 374, 917, 445, 673, 365, 953, 731, 760, 699, 608, 989, 291, 524, 271, 447, 545, 929, 104, 272, 617, 785, 81, 730, 452, 637,
                 161, 141, 945, 536, 819, 244, 333, 139, 746, 751, 364, 576, 178, 555, 637, 176, 975, 14, 233, 747, 832, 54, 251, 133, 177, 561, 14, 595,
                 908, 594, 90, 831, 258, 789, 335, 413, 149, 235, 586, 14, 328, 973, 945, 676, 824, 819, 825, 730, 513, 434, 985, 968, 202, 301, 146, 46,
                 761, 738, 68, 823, 449, 819, 341, 876, 697, 60, 617, 538, 756, 422, 873, 174, 30, 562, 998, 755, 817, 70, 630, 190, 154, 742, 164, 37, 158,
                 620, 465, 68, 403, 669, 306, 161, 333, 303, 599, 294, 449, 924, 196, 156, 426, 937, 234, 275, 443, 320, 516, 950, 397, 596, 271, 875, 703,
                 913, 205, 415, 4, 588, 27, 359, 560, 432, 14, 857, 866, 788, 778, 247, 466, 9, 57, 185, 158, 157, 380, 596, 381, 394, 7, 145, 574, 67, 37,
                 824, 588, 692, 816, 276, 960, 612, 335, 560, 904, 591, 854, 834, 800, 243, 833, 610, 448, 608, 883, 58, 63, 836, 158, 727, 772, 333, 52,
                 236, 537, 662, 114, 34, 250, 542, 317, 470, 564, 964, 178, 206, 911, 241, 229, 602, 456, 99, 546, 317, 626, 789, 542, 886, 53, 223, 379,
                 377, 497, 95, 868, 449, 17, 145, 536, 760, 758, 337, 745, 816, 507, 565, 49, 266, 392, 759, 85, 216, 374, 638, 677, 330, 569, 905, 667,
                 630, 555, 500, 890, 260, 400, 650, 702, 480, 2, 68, 214, 106, 865, 418, 336, 133, 83, 166, 612, 880, 940, 421, 300, 832, 241, 169, 26, 17,
                 316, 136, 648, 635, 689, 941, 66, 85, 30, 727, 293, 113, 327, 164, 199, 37, 153, 409, 829, 231, 70, 566, 565, 294, 926, 961, 167, 28, 197,
                 921, 889, 591, 188, 524, 251, 500, 205, 628, 785, 591, 929, 586, 789, 649, 916, 899, 669, 429, 880, 473, 636, 931, 442, 570, 101, 451, 760,
                 938, 387, 409, 214, 676, 346, 761, 513, 241, 209, 455, 597, 999, 403, 699, 657, 22, 146, 115, 44, 608, 339, 203, 570, 519, 516, 582, 265,
                 537, 437, 331, 314, 158, 440, 242, 477, 637, 553, 953, 759, 518, 239, 334, 975, 635, 714, 86, 668, 834, 963, 315, 511, 279, 648, 833, 813,
                 674, 430, 3, 150, 388, 82, 774, 360, 836, 955, 572, 342, 834, 507, 895, 734, 812, 577, 530, 110, 13, 696, 45, 330, 716, 975, 357, 515, 598,
                 149, 876, 27, 181, 439, 588, 684, 354, 423, 975, 81, 818, 584, 485, 215, 473, 843, 207, 708, 796, 707, 504, 408, 15, 866, 861, 489, 387,
                 418, 89, 608, 606, 716, 463, 335, 467, 825, 334, 529, 360, 111, 859, 390, 333, 514, 432, 186, 879, 505, 346, 258, 652, 596, 946, 845, 432,
                 756, 342, 237, 296, 36, 820, 19, 808, 761, 852, 42, 863, 583, 99, 177, 840, 861, 494, 842, 319, 304, 435, 633, 538, 63, 561, 404, 138, 214,
                 71, 555, 169, 434, 472, 239, 256, 805, 671, 428, 955, 869, 278, 867, 557, 596, 191, 759, 894, 877, 96, 574, 185, 864, 303, 703, 642, 309,
                 789, 359, 90, 78, 855, 516, 236, 152, 62, 231, 9, 507, 690, 37, 730, 593, 999, 397, 842, 578, 701, 936, 490, 382, 316, 480, 382, 642, 111,
                 762, 979, 654, 35, 231, 325, 534, 870, 119, 806, 748, 669, 150, 944, 797, 103, 22, 172, 86, 925, 474, 310, 901, 553, 228, 263, 194, 695,
                 467, 585, 692, 32, 891, 715, 262, 580, 752, 106, 314, 114, 976, 198, 610, 925, 793, 849, 405, 139, 306, 881, 624, 947, 784, 763, 428, 786,
                 605, 575, 324, 978, 132, 528, 719, 758, 586, 775, 840, 54, 720, 126, 391, 764, 992, 794, 12, 948, 156, 19, 677, 558, 414, 405, 394, 716,
                 465, 384, 148, 550, 654, 22, 50, 310, 24, 340, 112, 736, 756, 112, 577, 773, 437, 64, 175, 10, 912, 520, 961, 158, 857, 101, 962, 353, 334,
                 533, 753, 917, 438, 291, 653, 41, 613, 6, 385, 878, 153, 458, 286, 631, 999, 78, 765, 104, 693, 351, 440, 637, 615, 860, 58, 751, 335, 325,
                 193, 879, 123, 175, 233, 43, 873, 36, 961, 417, 107, 54, 630, 706, 953, 519, 683, 164, 896, 384, 501, 474, 14, 815, 797, 283, 340, 730, 254,
                 94, 814, 507, 435, 700, 809, 305, 651, 961, 262, 587, 170, 486, 244, 337, 471, 757, 118, 497, 183, 398, 47, 259, 955, 591, 964, 491, 886,
                 761, 157, 176, 430, 53, 256, 857, 823, 161, 442, 875, 379, 520, 733, 191, 647, 820, 73, 878, 400, 706, 383, 778, 301, 309, 818, 57, 306, 724,
                 288, 735, 700, 95, 605, 817, 664, 878, 356, 817, 111, 627, 917, 659, 172, 980, 571, 431, 533, 725, 188, 183, 754, 898, 552, 4, 176, 51, 306,
                 862, 355, 456, 735, 758, 656, 75, 446, 780, 118, 258, 846, 976, 19, 609, 630, 601, 918, 657, 473, 846, 810, 160, 191, 466, 657, 834, 746,
                 167, 818, 11, 688, 358, 197, 635, 452, 239, 2, 959, 282, 196, 227, 766, 309, 669, 270, 820, 644, 187, 409, 594, 762, 815, 771, 820, 245,
                 58, 283, 282, 693, 906, 595, 319, 790, 915, 806, 138, 940, 797, 785, 221, 873, 107, 36, 958, 590, 71, 853, 311, 420, 873, 931, 894, 761,
                 778, 299, 79, 346, 629, 788, 259, 183, 233, 395, 900, 827, 43, 387, 935, 269, 37, 254, 687, 198, 800, 150, 890, 58, 681, 891, 437, 916,
                 57, 420, 962, 153, 893, 6, 598, 934, 415, 441, 254, 630, 1, 748, 610, 63, 32, 960, 831, 945, 963, 775, 781, 308, 671, 214, 126, 930, 689,
                 446, 265, 163, 840, 1001, 189, 463, 49, 426]
        
        loss = largest_loss(huge_list)
        self.assertEqual(loss, 1000)

    def test_largest_loss_extremely_large_list(self):
        extreme_list = [783, 174, 670, 315, 801, 425, 329, 886, 787, 454, 803, 746, 539, 440, 265, 450, 863, 557, 819, 160, 428, 145, 618, 54, 232, 908, 82, 541,
                 751, 886, 144, 459, 737, 433, 980, 704, 859, 643, 908, 496, 659, 750, 557, 649, 997, 454, 998, 400, 956, 999, 917, 563, 74, 65, 992, 250,
                 719, 350, 487, 927, 400, 306, 318, 805, 330, 812, 43, 590, 582, 771, 506, 946, 345, 10, 923, 119, 776, 748, 770, 798, 545, 198, 167, 571,
                 537, 875, 156, 655, 68, 833, 761, 883, 61, 435, 584, 664, 548, 50, 857, 339, 637, 967, 607, 109, 600, 229, 694, 635, 755, 682, 4, 801, 152,
                 442, 738, 388, 196, 571, 957, 718, 867, 351, 176, 942, 935, 739, 28, 699, 674, 594, 408, 919, 446, 830, 526, 607, 651, 493, 443, 277, 297,
                 670, 683, 203, 110, 317, 389, 408, 70, 875, 102, 829, 750, 782, 508, 368, 651, 185, 27, 975, 306, 673, 872, 273, 403, 41, 141, 203, 789,
                 124, 598, 319, 990, 223, 108, 592, 56, 123, 337, 474, 705, 949, 104, 14, 264, 524, 959, 885, 663, 239, 998, 746, 472, 766, 195, 277, 113,
                 714, 578, 312, 837, 433, 941, 158, 91, 460, 27, 940, 227, 531, 562, 626, 88, 709, 315, 884, 856, 410, 439, 13, 744, 686, 473, 451, 126,
                 178, 254, 978, 593, 7, 540, 642, 490, 465, 82, 656, 709, 222, 908, 935, 953, 806, 568, 771, 236, 702, 482, 761, 753, 720, 387, 396, 201,
                 564, 477, 168, 151, 865, 774, 801, 123, 544, 142, 260, 610, 863, 394, 237, 381, 486, 374, 384, 62, 198, 727, 753, 739, 65, 919, 492, 733,
                 92, 59, 715, 374, 917, 445, 673, 365, 953, 731, 760, 699, 608, 989, 291, 524, 271, 447, 545, 929, 104, 272, 617, 785, 81, 730, 452, 637,
                 161, 141, 945, 536, 819, 244, 333, 139, 746, 751, 364, 576, 178, 555, 637, 176, 975, 14, 233, 747, 832, 54, 251, 133, 177, 561, 14, 595,
                 908, 594, 90, 831, 258, 789, 335, 413, 149, 235, 586, 14, 328, 973, 945, 676, 824, 819, 825, 730, 513, 434, 985, 968, 202, 301, 146, 46,
                 761, 738, 68, 823, 449, 819, 341, 876, 697, 60, 617, 538, 756, 422, 873, 174, 30, 562, 998, 755, 817, 70, 630, 190, 154, 742, 164, 37, 158,
                 620, 465, 68, 403, 669, 306, 161, 333, 303, 599, 294, 449, 924, 196, 156, 426, 937, 234, 275, 443, 320, 516, 950, 397, 596, 271, 875, 703,
                 913, 205, 415, 4, 588, 27, 359, 560, 432, 14, 857, 866, 788, 778, 247, 466, 9, 57, 185, 158, 157, 380, 596, 381, 394, 7, 145, 574, 67, 37,
                 824, 588, 692, 816, 276, 960, 612, 335, 560, 904, 591, 854, 834, 800, 243, 833, 610, 448, 608, 883, 58, 63, 836, 158, 727, 772, 333, 52,
                 236, 537, 662, 114, 34, 250, 542, 317, 470, 564, 964, 178, 206, 911, 241, 229, 602, 456, 99, 546, 317, 626, 789, 542, 886, 53, 223, 379,
                 377, 497, 95, 868, 449, 17, 145, 536, 760, 758, 337, 745, 816, 507, 565, 49, 266, 392, 759, 85, 216, 374, 638, 677, 330, 569, 905, 667,
                 630, 555, 500, 890, 260, 400, 650, 702, 480, 2, 68, 214, 106, 865, 418, 336, 133, 83, 166, 612, 880, 940, 421, 300, 832, 241, 169, 26, 17,
                 316, 136, 648, 635, 689, 941, 66, 85, 30, 727, 293, 113, 327, 164, 199, 37, 153, 409, 829, 231, 70, 566, 565, 294, 926, 961, 167, 28, 197,
                 921, 889, 591, 188, 524, 251, 500, 205, 628, 785, 591, 929, 586, 789, 649, 916, 899, 669, 429, 880, 473, 636, 931, 442, 570, 101, 451, 760,
                 938, 387, 409, 214, 676, 346, 761, 513, 241, 209, 455, 597, 999, 403, 699, 657, 22, 146, 115, 44, 608, 339, 203, 570, 519, 516, 582, 265,
                 537, 437, 331, 314, 158, 440, 242, 477, 637, 553, 953, 759, 518, 239, 334, 975, 635, 714, 86, 668, 834, 963, 315, 511, 279, 648, 833, 813,
                 674, 430, 3, 150, 388, 82, 774, 360, 836, 955, 572, 342, 834, 507, 895, 734, 812, 577, 530, 110, 13, 696, 45, 330, 716, 975, 357, 515, 598,
                 149, 876, 27, 181, 439, 588, 684, 354, 423, 975, 81, 818, 584, 485, 215, 473, 843, 207, 708, 796, 707, 504, 408, 15, 866, 861, 489, 387,
                 418, 89, 608, 606, 716, 463, 335, 467, 825, 334, 529, 360, 111, 859, 390, 333, 514, 432, 186, 879, 505, 346, 258, 652, 596, 946, 845, 432,
                 756, 342, 237, 296, 36, 820, 19, 808, 761, 852, 42, 863, 583, 99, 177, 840, 861, 494, 842, 319, 304, 435, 633, 538, 63, 561, 404, 138, 214,
                 71, 555, 169, 434, 472, 239, 256, 805, 671, 428, 955, 869, 278, 867, 557, 596, 191, 759, 894, 877, 96, 574, 185, 864, 303, 703, 642, 309,
                 789, 359, 90, 78, 855, 516, 236, 152, 783, 174, 670, 315, 801, 425, 329, 886, 787, 454, 803, 746, 539, 440, 265, 450, 863, 557, 819, 160, 428, 145, 618, 54, 232, 908, 82, 541,
                 751, 886, 144, 459, 737, 433, 980, 704, 859, 643, 908, 496, 659, 750, 557, 649, 997, 454, 998, 400, 956, 999, 917, 563, 74, 65, 992, 250,
                 719, 350, 487, 927, 400, 306, 318, 805, 330, 812, 43, 590, 582, 771, 506, 946, 345, 10, 923, 119, 776, 748, 770, 798, 545, 198, 167, 571,
                 537, 875, 156, 655, 68, 833, 761, 883, 61, 435, 584, 664, 548, 50, 857, 339, 637, 967, 607, 109, 600, 229, 694, 635, 755, 682, 4, 801, 152,
                 442, 738, 388, 196, 571, 957, 718, 867, 351, 176, 942, 935, 739, 28, 699, 674, 594, 408, 919, 446, 830, 526, 607, 651, 493, 443, 277, 297,
                 670, 683, 203, 110, 317, 389, 408, 70, 875, 102, 829, 750, 782, 508, 368, 651, 185, 27, 975, 306, 673, 872, 273, 403, 41, 141, 203, 789,
                 124, 598, 319, 990, 223, 108, 592, 56, 123, 337, 474, 705, 949, 104, 14, 264, 524, 959, 885, 663, 239, 998, 746, 472, 766, 195, 277, 113,
                 714, 578, 312, 837, 433, 941, 158, 91, 460, 27, 940, 227, 531, 562, 626, 88, 709, 315, 884, 856, 410, 439, 13, 744, 686, 473, 451, 126,
                 178, 254, 978, 593, 7, 540, 642, 490, 465, 82, 656, 709, 222, 908, 935, 953, 806, 568, 771, 236, 702, 482, 761, 753, 720, 387, 396, 201,
                 564, 477, 168, 151, 865, 774, 801, 123, 544, 142, 260, 610, 863, 394, 237, 381, 486, 374, 384, 62, 198, 727, 753, 739, 65, 919, 492, 733,
                 92, 59, 715, 374, 917, 445, 673, 365, 953, 731, 760, 699, 608, 989, 291, 524, 271, 447, 545, 929, 104, 272, 617, 785, 81, 730, 452, 637,
                 161, 141, 945, 536, 819, 244, 333, 139, 746, 751, 364, 576, 178, 555, 637, 176, 975, 14, 233, 747, 832, 54, 251, 133, 177, 561, 14, 595,
                 908, 594, 90, 831, 258, 789, 335, 413, 149, 235, 586, 14, 328, 973, 945, 676, 824, 819, 825, 730, 513, 434, 985, 968, 202, 301, 146, 46,
                 761, 738, 68, 823, 449, 819, 341, 876, 697, 60, 617, 538, 756, 422, 873, 174, 30, 562, 998, 755, 817, 70, 630, 190, 154, 742, 164, 37, 158,
                 620, 465, 68, 403, 669, 306, 161, 333, 303, 599, 294, 449, 924, 196, 156, 426, 937, 234, 275, 443, 320, 516, 950, 397, 596, 271, 875, 703,
                 913, 205, 415, 4, 588, 27, 359, 560, 432, 14, 857, 866, 788, 778, 247, 466, 9, 57, 185, 158, 157, 380, 596, 381, 394, 7, 145, 574, 67, 37,
                 824, 588, 692, 816, 276, 960, 612, 335, 560, 904, 591, 854, 834, 800, 243, 833, 610, 448, 608, 883, 58, 63, 836, 158, 727, 772, 333, 52,
                 236, 537, 662, 114, 34, 250, 542, 317, 470, 564, 964, 178, 206, 911, 241, 229, 602, 456, 99, 546, 317, 626, 789, 542, 886, 53, 223, 379,
                 377, 497, 95, 868, 449, 17, 145, 536, 760, 758, 337, 745, 816, 507, 565, 49, 266, 392, 759, 85, 216, 374, 638, 677, 330, 569, 905, 667,
                 630, 555, 500, 890, 260, 400, 650, 702, 480, 2, 68, 214, 106, 865, 418, 336, 133, 83, 166, 612, 880, 940, 421, 300, 832, 241, 169, 26, 17,
                 316, 136, 648, 635, 689, 941, 66, 85, 30, 727, 293, 113, 327, 164, 199, 37, 153, 409, 829, 231, 70, 566, 565, 294, 926, 961, 167, 28, 197,
                 921, 889, 591, 188, 524, 251, 500, 205, 628, 785, 591, 929, 586, 789, 649, 916, 899, 669, 429, 880, 473, 636, 931, 442, 570, 101, 451, 760,
                 938, 387, 409, 214, 676, 346, 761, 513, 241, 209, 455, 597, 999, 403, 699, 657, 22, 146, 115, 44, 608, 339, 203, 570, 519, 516, 582, 265,
                 537, 437, 331, 314, 158, 440, 242, 477, 637, 553, 953, 759, 518, 239, 334, 975, 635, 714, 86, 668, 834, 963, 315, 511, 279, 648, 833, 813,
                 674, 430, 3, 150, 388, 82, 774, 360, 836, 955, 572, 342, 834, 507, 895, 734, 812, 577, 530, 110, 13, 696, 45, 330, 716, 975, 357, 515, 598,
                 149, 876, 27, 181, 439, 588, 684, 354, 423, 975, 81, 818, 584, 485, 215, 473, 843, 207, 708, 796, 707, 504, 408, 15, 866, 861, 489, 387,
                 418, 89, 608, 606, 716, 463, 335, 467, 825, 334, 529, 360, 111, 859, 390, 333, 514, 432, 186, 879, 505, 346, 258, 652, 596, 946, 845, 432,
                 756, 342, 237, 296, 36, 820, 19, 808, 761, 852, 42, 863, 583, 99, 177, 840, 861, 494, 842, 319, 304, 435, 633, 538, 63, 561, 404, 138, 214,
                 71, 555, 169, 434, 472, 239, 256, 805, 671, 428, 955, 869, 278, 867, 557, 596, 191, 759, 894, 877, 96, 574, 185, 864, 303, 703, 642, 309,
                 789, 359, 90, 78, 855, 516, 236, 152, 783, 174, 670, 315, 801, 425, 329, 886, 787, 454, 803, 746, 539, 440, 265, 450, 863, 557, 819, 160, 428, 145, 618, 54, 232, 908, 82, 541,
                 751, 886, 144, 459, 737, 433, 980, 704, 859, 643, 908, 496, 659, 750, 557, 649, 997, 454, 998, 400, 956, 999, 917, 563, 74, 65, 992, 250,
                 719, 350, 487, 927, 400, 306, 318, 805, 330, 812, 43, 590, 582, 771, 506, 946, 345, 10, 923, 119, 776, 748, 770, 798, 545, 198, 167, 571,
                 537, 875, 156, 655, 68, 833, 761, 883, 61, 435, 584, 664, 548, 50, 857, 339, 637, 967, 607, 109, 600, 229, 694, 635, 755, 682, 4, 801, 152,
                 442, 738, 388, 196, 571, 957, 718, 867, 351, 176, 942, 935, 739, 28, 699, 674, 594, 408, 919, 446, 830, 526, 607, 651, 493, 443, 277, 297,
                 670, 683, 203, 110, 317, 389, 408, 70, 875, 102, 829, 750, 782, 508, 368, 651, 185, 27, 975, 306, 673, 872, 273, 403, 41, 141, 203, 789,
                 124, 598, 319, 990, 223, 108, 592, 56, 123, 337, 474, 705, 949, 104, 14, 264, 524, 959, 885, 663, 239, 998, 746, 472, 766, 195, 277, 113,
                 714, 578, 312, 837, 433, 941, 158, 91, 460, 27, 940, 227, 531, 562, 626, 88, 709, 315, 884, 856, 410, 439, 13, 744, 686, 473, 451, 126,
                 178, 254, 978, 593, 7, 540, 642, 490, 465, 82, 656, 709, 222, 908, 935, 953, 806, 568, 771, 236, 702, 482, 761, 753, 720, 387, 396, 201,
                 564, 477, 168, 151, 865, 774, 801, 123, 544, 142, 260, 610, 863, 394, 237, 381, 486, 374, 384, 62, 198, 727, 753, 739, 65, 919, 492, 733,
                 92, 59, 715, 374, 917, 445, 673, 365, 953, 731, 760, 699, 608, 989, 291, 524, 271, 447, 545, 929, 104, 272, 617, 785, 81, 730, 452, 637,
                 161, 141, 945, 536, 819, 244, 333, 139, 746, 751, 364, 576, 178, 555, 637, 176, 975, 14, 233, 747, 832, 54, 251, 133, 177, 561, 14, 595,
                 908, 594, 90, 831, 258, 789, 335, 413, 149, 235, 586, 14, 328, 973, 945, 676, 824, 819, 825, 730, 513, 434, 985, 968, 202, 301, 146, 46,
                 761, 738, 68, 823, 449, 819, 341, 876, 697, 60, 617, 538, 756, 422, 873, 174, 30, 562, 998, 755, 817, 70, 630, 190, 154, 742, 164, 37, 158,
                 620, 465, 68, 403, 669, 306, 161, 333, 303, 599, 294, 449, 924, 196, 156, 426, 937, 234, 275, 443, 320, 516, 950, 397, 596, 271, 875, 703,
                 913, 205, 415, 4, 588, 27, 359, 560, 432, 14, 857, 866, 788, 778, 247, 466, 9, 57, 185, 158, 157, 380, 596, 381, 394, 7, 145, 574, 67, 37,
                 824, 588, 692, 816, 276, 960, 612, 335, 560, 904, 591, 854, 834, 800, 243, 833, 610, 448, 608, 883, 58, 63, 836, 158, 727, 772, 333, 52,
                 236, 537, 662, 114, 34, 250, 542, 317, 470, 564, 964, 178, 206, 911, 241, 229, 602, 456, 99, 546, 317, 626, 789, 542, 886, 53, 223, 379,
                 377, 497, 95, 868, 449, 17, 145, 536, 760, 758, 337, 745, 816, 507, 565, 49, 266, 392, 759, 85, 216, 374, 638, 677, 330, 569, 905, 667,
                 630, 555, 500, 890, 260, 400, 650, 702, 480, 2, 68, 214, 106, 865, 418, 336, 133, 83, 166, 612, 880, 940, 421, 300, 832, 241, 169, 26, 17,
                 316, 136, 648, 635, 689, 941, 66, 85, 30, 727, 293, 113, 327, 164, 199, 37, 153, 409, 829, 231, 70, 566, 565, 294, 926, 961, 167, 28, 197,
                 921, 889, 591, 188, 524, 251, 500, 205, 628, 785, 591, 929, 586, 789, 649, 916, 899, 669, 429, 880, 473, 636, 931, 442, 570, 101, 451, 760,
                 938, 387, 409, 214, 676, 346, 761, 513, 241, 209, 455, 597, 999, 403, 699, 657, 22, 146, 115, 44, 608, 339, 203, 570, 519, 516, 582, 265,
                 537, 437, 331, 314, 158, 440, 242, 477, 637, 553, 953, 759, 518, 239, 334, 975, 635, 714, 86, 668, 834, 963, 315, 511, 279, 648, 833, 813,
                 674, 430, 3, 150, 388, 82, 774, 360, 836, 955, 572, 342, 834, 507, 895, 734, 812, 577, 530, 110, 13, 696, 45, 330, 716, 975, 357, 515, 598,
                 149, 876, 27, 181, 439, 588, 684, 354, 423, 975, 81, 818, 584, 485, 215, 473, 843, 207, 708, 796, 707, 504, 408, 15, 866, 861, 489, 387,
                 418, 89, 608, 606, 716, 463, 335, 467, 825, 334, 529, 360, 111, 859, 390, 333, 514, 432, 186, 879, 505, 346, 258, 652, 596, 946, 845, 432,
                 756, 342, 237, 296, 36, 820, 19, 808, 761, 852, 42, 863, 583, 99, 177, 840, 861, 494, 842, 319, 304, 435, 633, 538, 63, 561, 404, 138, 214,
                 71, 555, 169, 434, 472, 239, 256, 805, 671, 428, 955, 869, 278, 867, 557, 596, 191, 759, 894, 877, 96, 574, 185, 864, 303, 703, 642, 309,
                 789, 359, 90, 78, 855, 516, 236, 152, 783, 174, 670, 315, 801, 425, 329, 886, 787, 454, 803, 746, 539, 440, 265, 450, 863, 557, 819, 160, 428, 145, 618, 54, 232, 908, 82, 541,
                 751, 886, 144, 459, 737, 433, 980, 704, 859, 643, 908, 496, 659, 750, 557, 649, 997, 454, 998, 400, 956, 999, 917, 563, 74, 65, 992, 250,
                 719, 350, 487, 927, 400, 306, 318, 805, 330, 812, 43, 590, 582, 771, 506, 946, 345, 10, 923, 119, 776, 748, 770, 798, 545, 198, 167, 571,
                 537, 875, 156, 655, 68, 833, 761, 883, 61, 435, 584, 664, 548, 50, 857, 339, 637, 967, 607, 109, 600, 229, 694, 635, 755, 682, 4, 801, 152,
                 442, 738, 388, 196, 571, 957, 718, 867, 351, 176, 942, 935, 739, 28, 699, 674, 594, 408, 919, 446, 830, 526, 607, 651, 493, 443, 277, 297,
                 670, 683, 203, 110, 317, 389, 408, 70, 875, 102, 829, 750, 782, 508, 368, 651, 185, 27, 975, 306, 673, 872, 273, 403, 41, 141, 203, 789,
                 124, 598, 319, 990, 223, 108, 592, 56, 123, 337, 474, 705, 949, 104, 14, 264, 524, 959, 885, 663, 239, 998, 746, 472, 766, 195, 277, 113,
                 714, 578, 312, 837, 433, 941, 158, 91, 460, 27, 940, 227, 531, 562, 626, 88, 709, 315, 884, 856, 410, 439, 13, 744, 686, 473, 451, 126,
                 178, 254, 978, 593, 7, 540, 642, 490, 465, 82, 656, 709, 222, 908, 935, 953, 806, 568, 771, 236, 702, 482, 761, 753, 720, 387, 396, 201,
                 564, 477, 168, 151, 865, 774, 801, 123, 544, 142, 260, 610, 863, 394, 237, 381, 486, 374, 384, 62, 198, 727, 753, 739, 65, 919, 492, 733,
                 92, 59, 715, 374, 917, 445, 673, 365, 953, 731, 760, 699, 608, 989, 291, 524, 271, 447, 545, 929, 104, 272, 617, 785, 81, 730, 452, 637,
                 161, 141, 945, 536, 819, 244, 333, 139, 746, 751, 364, 576, 178, 555, 637, 176, 975, 14, 233, 747, 832, 54, 251, 133, 177, 561, 14, 595,
                 908, 594, 90, 831, 258, 789, 335, 413, 149, 235, 586, 14, 328, 973, 945, 676, 824, 819, 825, 730, 513, 434, 985, 968, 202, 301, 146, 46,
                 761, 738, 68, 823, 449, 819, 341, 876, 697, 60, 617, 538, 756, 422, 873, 174, 30, 562, 998, 755, 817, 70, 630, 190, 154, 742, 164, 37, 158,
                 620, 465, 68, 403, 669, 306, 161, 333, 303, 599, 294, 449, 924, 196, 156, 426, 937, 234, 275, 443, 320, 516, 950, 397, 596, 271, 875, 703,
                 913, 205, 415, 4, 588, 27, 359, 560, 432, 14, 857, 866, 788, 778, 247, 466, 9, 57, 185, 158, 157, 380, 596, 381, 394, 7, 145, 574, 67, 37,
                 824, 588, 692, 816, 276, 960, 612, 335, 560, 904, 591, 854, 834, 800, 243, 833, 610, 448, 608, 883, 58, 63, 836, 158, 727, 772, 333, 52,
                 236, 537, 662, 114, 34, 250, 542, 317, 470, 564, 964, 178, 206, 911, 241, 229, 602, 456, 99, 546, 317, 626, 789, 542, 886, 53, 223, 379,
                 377, 497, 95, 868, 449, 17, 145, 536, 760, 758, 337, 745, 816, 507, 565, 49, 266, 392, 759, 85, 216, 374, 638, 677, 330, 569, 905, 667,
                 630, 555, 500, 890, 260, 400, 650, 702, 480, 2, 68, 214, 106, 865, 418, 336, 133, 83, 166, 612, 880, 940, 421, 300, 832, 241, 169, 26, 17,
                 316, 136, 648, 635, 689, 941, 66, 85, 30, 727, 293, 113, 327, 164, 199, 37, 153, 409, 829, 231, 70, 566, 565, 294, 926, 961, 167, 28, 197,
                 921, 889, 591, 188, 524, 251, 500, 205, 628, 785, 591, 929, 586, 789, 649, 916, 899, 669, 429, 880, 473, 636, 931, 442, 570, 101, 451, 760,
                 938, 387, 409, 214, 676, 346, 761, 513, 241, 209, 455, 597, 999, 403, 699, 657, 22, 146, 115, 44, 608, 339, 203, 570, 519, 516, 582, 265,
                 537, 437, 331, 314, 158, 440, 242, 477, 637, 553, 953, 759, 518, 239, 334, 975, 635, 714, 86, 668, 834, 963, 315, 511, 279, 648, 833, 813,
                 674, 430, 3, 150, 388, 82, 774, 360, 836, 955, 572, 342, 834, 507, 895, 734, 812, 577, 530, 110, 13, 696, 45, 330, 716, 975, 357, 515, 598,
                 149, 876, 27, 181, 439, 588, 684, 354, 423, 975, 81, 818, 584, 485, 215, 473, 843, 207, 708, 796, 707, 504, 408, 15, 866, 861, 489, 387,
                 418, 89, 608, 606, 716, 463, 335, 467, 825, 334, 529, 360, 111, 859, 390, 333, 514, 432, 186, 879, 505, 346, 258, 652, 596, 946, 845, 432,
                 756, 342, 237, 296, 36, 820, 19, 808, 761, 852, 42, 863, 583, 99, 177, 840, 861, 494, 842, 319, 304, 435, 633, 538, 63, 561, 404, 138, 214,
                 71, 555, 169, 434, 472, 239, 256, 805, 671, 428, 955, 869, 278, 867, 557, 596, 191, 759, 894, 877, 96, 574, 185, 864, 303, 703, 642, 309,
                 789, 359, 90, 78, 855, 516, 236, 152, 783, 174, 670, 315, 801, 425, 329, 886, 787, 454, 803, 746, 539, 440, 265, 450, 863, 557, 819, 160, 428, 145, 618, 54, 232, 908, 82, 541,
                 751, 886, 144, 459, 737, 433, 980, 704, 859, 643, 908, 496, 659, 750, 557, 649, 997, 454, 998, 400, 956, 999, 917, 563, 74, 65, 992, 250,
                 719, 350, 487, 927, 400, 306, 318, 805, 330, 812, 43, 590, 582, 771, 506, 946, 345, 10, 923, 119, 776, 748, 770, 798, 545, 198, 167, 571,
                 537, 875, 156, 655, 68, 833, 761, 883, 61, 435, 584, 664, 548, 50, 857, 339, 637, 967, 607, 109, 600, 229, 694, 635, 755, 682, 4, 801, 152,
                 442, 738, 388, 196, 571, 957, 718, 867, 351, 176, 942, 935, 739, 28, 699, 674, 594, 408, 919, 446, 830, 526, 607, 651, 493, 443, 277, 297,
                 670, 683, 203, 110, 317, 389, 408, 70, 875, 102, 829, 750, 782, 508, 368, 651, 185, 27, 975, 306, 673, 872, 273, 403, 41, 141, 203, 789,
                 124, 598, 319, 990, 223, 108, 592, 56, 123, 337, 474, 705, 949, 104, 14, 264, 524, 959, 885, 663, 239, 998, 746, 472, 766, 195, 277, 113,
                 714, 578, 312, 837, 433, 941, 158, 91, 460, 27, 940, 227, 531, 562, 626, 88, 709, 315, 884, 856, 410, 439, 13, 744, 686, 473, 451, 126,
                 178, 254, 978, 593, 7, 540, 642, 490, 465, 82, 656, 709, 222, 908, 935, 953, 806, 568, 771, 236, 702, 482, 761, 753, 720, 387, 396, 201,
                 564, 477, 168, 151, 865, 774, 801, 123, 544, 142, 260, 610, 863, 394, 237, 381, 486, 374, 384, 62, 198, 727, 753, 739, 65, 919, 492, 733,
                 92, 59, 715, 374, 917, 445, 673, 365, 953, 731, 760, 699, 608, 989, 291, 524, 271, 447, 545, 929, 104, 272, 617, 785, 81, 730, 452, 637,
                 161, 141, 945, 536, 819, 244, 333, 139, 746, 751, 364, 576, 178, 555, 637, 176, 975, 14, 233, 747, 832, 54, 251, 133, 177, 561, 14, 595,
                 908, 594, 90, 831, 258, 789, 335, 413, 149, 235, 586, 14, 328, 973, 945, 676, 824, 819, 825, 730, 513, 434, 985, 968, 202, 301, 146, 46,
                 761, 738, 68, 823, 449, 819, 341, 876, 697, 60, 617, 538, 756, 422, 873, 174, 30, 562, 998, 755, 817, 70, 630, 190, 154, 742, 164, 37, 158,
                 620, 465, 68, 403, 669, 306, 161, 333, 303, 599, 294, 449, 924, 196, 156, 426, 937, 234, 275, 443, 320, 516, 950, 397, 596, 271, 875, 703,
                 913, 205, 415, 4, 588, 27, 359, 560, 432, 14, 857, 866, 788, 778, 247, 466, 9, 57, 185, 158, 157, 380, 596, 381, 394, 7, 145, 574, 67, 37,
                 824, 588, 692, 816, 276, 960, 612, 335, 560, 904, 591, 854, 834, 800, 243, 833, 610, 448, 608, 883, 58, 63, 836, 158, 727, 772, 333, 52,
                 236, 537, 662, 114, 34, 250, 542, 317, 470, 564, 964, 178, 206, 911, 241, 229, 602, 456, 99, 546, 317, 626, 789, 542, 886, 53, 223, 379,
                 377, 497, 95, 868, 449, 17, 145, 536, 760, 758, 337, 745, 816, 507, 565, 49, 266, 392, 759, 85, 216, 374, 638, 677, 330, 569, 905, 667,
                 630, 555, 500, 890, 260, 400, 650, 702, 480, 2, 68, 214, 106, 865, 418, 336, 133, 83, 166, 612, 880, 940, 421, 300, 832, 241, 169, 26, 17,
                 316, 136, 648, 635, 689, 941, 66, 85, 30, 727, 293, 113, 327, 164, 199, 37, 153, 409, 829, 231, 70, 566, 565, 294, 926, 961, 167, 28, 197,
                 921, 889, 591, 188, 524, 251, 500, 205, 628, 785, 591, 929, 586, 789, 649, 916, 899, 669, 429, 880, 473, 636, 931, 442, 570, 101, 451, 760,
                 938, 387, 409, 214, 676, 346, 761, 513, 241, 209, 455, 597, 999, 403, 699, 657, 22, 146, 115, 44, 608, 339, 203, 570, 519, 516, 582, 265,
                 537, 437, 331, 314, 158, 440, 242, 477, 637, 553, 953, 759, 518, 239, 334, 975, 635, 714, 86, 668, 834, 963, 315, 511, 279, 648, 833, 813,
                 674, 430, 3, 150, 388, 82, 774, 360, 836, 955, 572, 342, 834, 507, 895, 734, 812, 577, 530, 110, 13, 696, 45, 330, 716, 975, 357, 515, 598,
                 149, 876, 27, 181, 439, 588, 684, 354, 423, 975, 81, 818, 584, 485, 215, 473, 843, 207, 708, 796, 707, 504, 408, 15, 866, 861, 489, 387,
                 418, 89, 608, 606, 716, 463, 335, 467, 825, 334, 529, 360, 111, 859, 390, 333, 514, 432, 186, 879, 505, 346, 258, 652, 596, 946, 845, 432,
                 756, 342, 237, 296, 36, 820, 19, 808, 761, 852, 42, 863, 583, 99, 177, 840, 861, 494, 842, 319, 304, 435, 633, 538, 63, 561, 404, 138, 214,
                 71, 555, 169, 434, 472, 239, 256, 805, 671, 428, 955, 869, 278, 867, 557, 596, 191, 759, 894, 877, 96, 574, 185, 864, 303, 703, 642, 309,
                 789, 359, 90, 78, 855, 516, 236, 152, 783, 174, 670, 315, 801, 425, 329, 886, 787, 454, 803, 746, 539, 440, 265, 450, 863, 557, 819, 160, 428, 145, 618, 54, 232, 908, 82, 541,
                 751, 886, 144, 459, 737, 433, 980, 704, 859, 643, 908, 496, 659, 750, 557, 649, 997, 454, 998, 400, 956, 999, 917, 563, 74, 65, 992, 250,
                 719, 350, 487, 927, 400, 306, 318, 805, 330, 812, 43, 590, 582, 771, 506, 946, 345, 10, 923, 119, 776, 748, 770, 798, 545, 198, 167, 571,
                 537, 875, 156, 655, 68, 833, 761, 883, 61, 435, 584, 664, 548, 50, 857, 339, 637, 967, 607, 109, 600, 229, 694, 635, 755, 682, 4, 801, 152,
                 442, 738, 388, 196, 571, 957, 718, 867, 351, 176, 942, 935, 739, 28, 699, 674, 594, 408, 919, 446, 830, 526, 607, 651, 493, 443, 277, 297,
                 670, 683, 203, 110, 317, 389, 408, 70, 875, 102, 829, 750, 782, 508, 368, 651, 185, 27, 975, 306, 673, 872, 273, 403, 41, 141, 203, 789,
                 124, 598, 319, 990, 223, 108, 592, 56, 123, 337, 474, 705, 949, 104, 14, 264, 524, 959, 885, 663, 239, 998, 746, 472, 766, 195, 277, 113,
                 714, 578, 312, 837, 433, 941, 158, 91, 460, 27, 940, 227, 531, 562, 626, 88, 709, 315, 884, 856, 410, 439, 13, 744, 686, 473, 451, 126,
                 178, 254, 978, 593, 7, 540, 642, 490, 465, 82, 656, 709, 222, 908, 935, 953, 806, 568, 771, 236, 702, 482, 761, 753, 720, 387, 396, 201,
                 564, 477, 168, 151, 865, 774, 801, 123, 544, 142, 260, 610, 863, 394, 237, 381, 486, 374, 384, 62, 198, 727, 753, 739, 65, 919, 492, 733,
                 92, 59, 715, 374, 917, 445, 673, 365, 953, 731, 760, 699, 608, 989, 291, 524, 271, 447, 545, 929, 104, 272, 617, 785, 81, 730, 452, 637,
                 161, 141, 945, 536, 819, 244, 333, 139, 746, 751, 364, 576, 178, 555, 637, 176, 975, 14, 233, 747, 832, 54, 251, 133, 177, 561, 14, 595,
                 908, 594, 90, 831, 258, 789, 335, 413, 149, 235, 586, 14, 328, 973, 945, 676, 824, 819, 825, 730, 513, 434, 985, 968, 202, 301, 146, 46,
                 761, 738, 68, 823, 449, 819, 341, 876, 697, 60, 617, 538, 756, 422, 873, 174, 30, 562, 998, 755, 817, 70, 630, 190, 154, 742, 164, 37, 158,
                 620, 465, 68, 403, 669, 306, 161, 333, 303, 599, 294, 449, 924, 196, 156, 426, 937, 234, 275, 443, 320, 516, 950, 397, 596, 271, 875, 703,
                 913, 205, 415, 4, 588, 27, 359, 560, 432, 14, 857, 866, 788, 778, 247, 466, 9, 57, 185, 158, 157, 380, 596, 381, 394, 7, 145, 574, 67, 37,
                 824, 588, 692, 816, 276, 960, 612, 335, 560, 904, 591, 854, 834, 800, 243, 833, 610, 448, 608, 883, 58, 63, 836, 158, 727, 772, 333, 52,
                 236, 537, 662, 114, 34, 250, 542, 317, 470, 564, 964, 178, 206, 911, 241, 229, 602, 456, 99, 546, 317, 626, 789, 542, 886, 53, 223, 379,
                 377, 497, 95, 868, 449, 17, 145, 536, 760, 758, 337, 745, 816, 507, 565, 49, 266, 392, 759, 85, 216, 374, 638, 677, 330, 569, 905, 667,
                 630, 555, 500, 890, 260, 400, 650, 702, 480, 2, 68, 214, 106, 865, 418, 336, 133, 83, 166, 612, 880, 940, 421, 300, 832, 241, 169, 26, 17,
                 316, 136, 648, 635, 689, 941, 66, 85, 30, 727, 293, 113, 327, 164, 199, 37, 153, 409, 829, 231, 70, 566, 565, 294, 926, 961, 167, 28, 197,
                 921, 889, 591, 188, 524, 251, 500, 205, 628, 785, 591, 929, 586, 789, 649, 916, 899, 669, 429, 880, 473, 636, 931, 442, 570, 101, 451, 760,
                 938, 387, 409, 214, 676, 346, 761, 513, 241, 209, 455, 597, 999, 403, 699, 657, 22, 146, 115, 44, 608, 339, 203, 570, 519, 516, 582, 265,
                 537, 437, 331, 314, 158, 440, 242, 477, 637, 553, 953, 759, 518, 239, 334, 975, 635, 714, 86, 668, 834, 963, 315, 511, 279, 648, 833, 813,
                 674, 430, 3, 150, 388, 82, 774, 360, 836, 955, 572, 342, 834, 507, 895, 734, 812, 577, 530, 110, 13, 696, 45, 330, 716, 975, 357, 515, 598,
                 149, 876, 27, 181, 439, 588, 684, 354, 423, 975, 81, 818, 584, 485, 215, 473, 843, 207, 708, 796, 707, 504, 408, 15, 866, 861, 489, 387,
                 418, 89, 608, 606, 716, 463, 335, 467, 825, 334, 529, 360, 111, 859, 390, 333, 514, 432, 186, 879, 505, 346, 258, 652, 596, 946, 845, 432,
                 756, 342, 237, 296, 36, 820, 19, 808, 761, 852, 42, 863, 583, 99, 177, 840, 861, 494, 842, 319, 304, 435, 633, 538, 63, 561, 404, 138, 214,
                 71, 555, 169, 434, 472, 239, 256, 805, 671, 428, 955, 869, 278, 867, 557, 596, 191, 759, 894, 877, 96, 574, 185, 864, 303, 703, 642, 309,
                 789, 359, 90, 78, 855, 516, 236, 152, 62, 231, 9, 507, 690, 37, 730, 593, 999, 397, 842, 578, 701, 936, 490, 382, 316, 480, 382, 642, 111,
                 762, 979, 654, 35, 231, 325, 534, 870, 119, 806, 748, 669, 150, 944, 797, 103, 22, 172, 86, 925, 474, 310, 901, 553, 228, 263, 194, 695,
                 467, 585, 692, 32, 891, 715, 262, 580, 752, 106, 314, 114, 976, 198, 610, 925, 793, 849, 405, 139, 306, 881, 624, 947, 784, 763, 428, 786,
                 605, 575, 324, 978, 132, 528, 719, 758, 586, 775, 840, 54, 720, 126, 391, 764, 992, 794, 12, 948, 156, 19, 677, 558, 414, 405, 394, 716,
                 465, 384, 148, 550, 654, 22, 50, 310, 24, 340, 112, 736, 756, 112, 577, 773, 437, 64, 175, 10, 912, 520, 961, 158, 857, 101, 962, 353, 334,
                 533, 753, 917, 438, 291, 653, 41, 613, 6, 385, 878, 153, 458, 286, 631, 999, 78, 765, 104, 693, 351, 440, 637, 615, 860, 58, 751, 335, 325,
                 193, 879, 123, 175, 233, 43, 873, 36, 961, 417, 107, 54, 630, 706, 953, 519, 683, 164, 896, 384, 501, 474, 14, 815, 797, 283, 340, 730, 254,
                 94, 814, 507, 435, 700, 809, 305, 651, 961, 262, 587, 170, 486, 244, 337, 471, 757, 118, 497, 183, 398, 47, 259, 955, 591, 964, 491, 886,
                 761, 157, 176, 430, 53, 256, 857, 823, 161, 442, 875, 379, 520, 733, 191, 647, 820, 73, 878, 400, 706, 383, 778, 301, 309, 818, 57, 306, 724,
                 288, 735, 700, 95, 605, 817, 664, 878, 356, 817, 111, 627, 917, 659, 172, 980, 571, 431, 533, 725, 188, 183, 754, 898, 552, 4, 176, 51, 306,
                 862, 355, 456, 735, 758, 656, 75, 446, 780, 118, 258, 846, 976, 19, 609, 630, 601, 918, 657, 473, 846, 810, 160, 191, 466, 657, 834, 746,
                 167, 818, 11, 688, 358, 197, 635, 452, 239, 2, 959, 282, 196, 227, 766, 309, 669, 270, 820, 644, 187, 409, 594, 762, 815, 771, 820, 245,
                 58, 283, 282, 693, 906, 595, 319, 790, 915, 806, 138, 940, 797, 785, 221, 873, 107, 36, 958, 590, 71, 853, 311, 420, 873, 931, 894, 761,
                 778, 299, 79, 346, 629, 788, 259, 183, 233, 395, 900, 827, 43, 387, 935, 269, 37, 254, 687, 198, 800, 150, 890, 58, 681, 891, 437, 916,
                 57, 420, 962, 153, 893, 6, 598, 934, 415, 441, 254, 630, 1, 748, 610, 63, 32, 960, 831, 945, 963, 775, 781, 308, 671, 214, 126, 930, 689,
                 446, 265, 163, 840, 1001, 189, 463, 49, 426]
        
        loss = largest_loss_brute(extreme_list)
        self.assertEqual(loss, 1000)

        

unittest.main()
