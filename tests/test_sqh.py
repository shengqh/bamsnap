import sys
import shlex

# sys.path.append('..')
# bamsnap_prog = "src/bamsnap.py"
# from bamsnap import bamsnap

from context import bamsnap
bamsnap_prog = "bamsnap"


cmdlist = []


cmdlist.append("""
    -bam /scratch/cqs/ravi_shah_projects/20220107_rnaseq_discovery_hg38/star_featurecount/result/P_AI120118_V1_Aligned.sortedByCoord.out.bam \
    -title "P_AI120118_V1" \
    -pos chr2:231921809-231926396 \
    -out /scratch/cqs/ravi_shah_projects/20220107_rnaseq_discovery_hg38/NPPC.png \
    -bamplot coverage read gene\
    -margin 100 \
    -no_target_line \
    -read_color_by interchrom \
    -save_image_only
""")


def test_run():
    for cmd in cmdlist:
        # cmd = cmdlist[-1]
        cmd = bamsnap_prog + " " + cmd.strip()
        sys.argv = shlex.split(cmd)
        print(' '.join(sys.argv))
        # print(cmd)
        # print(shlex.quote(sys.argv))
        bamsnap.cli()
        # break

if __name__ == "__main__":
    test_run()
