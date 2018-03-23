Writes all permutations of the LUT in "Editblk BA"
Result: the bits are spread out among multiple frames
but always have offset 36

diff sweep_clb_BA/out/0x00/SBAPR.bits sweep_clb_BA/out/0x0F/SBAPR.bits |fgrep _
    < 8b_36
    < 8d_36
    < 90_36
    < 9b_36
diff sweep_clb_BA/out/0x00/SBAPR.bits sweep_clb_BA/out/0x01/SBAPR.bits |fgrep _
    < 8b_36
diff sweep_clb_BA/out/0x00/SBAPR.bits sweep_clb_BA/out/0x02/SBAPR.bits |fgrep _
    < 9b_36
diff sweep_clb_BA/out/0x00/SBAPR.bits sweep_clb_BA/out/0x04/SBAPR.bits |fgrep _
    < 8d_36
diff sweep_clb_BA/out/0x00/SBAPR.bits sweep_clb_BA/out/0x08/SBAPR.bits |fgrep _
    < 90_36

Luts are lettered NM N and M are letters A...H




