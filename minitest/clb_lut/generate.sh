python generate.py

(
for i in $(seq 1 15); do \
    h1="0001"; \
    h2=$(printf "%04X" $((1 << $i))); \
    echo ; \
    echo $h1 $h2; \
    diff out_{$h1,$h2}/DESIGN.BITS |fgrep _ ; \
done
) |tee out.txt


