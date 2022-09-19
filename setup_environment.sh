export env_name="jwst_validation_notebooks"
export TEST_BIGDATA="https://bytesalad.stsci.edu/artifactory"
export CRDS_SERVER_URL="https://jwst-crds.stsci.edu"
export CRDS_PATH="/grp/crds/cache"
export WIT4_PATH="/grp/jwst/wit4"
export PIPELINE_VERSION=$(<pipeline_version.txt)

case `uname` in
    Darwin)
        if ! command -v conda &> /dev/null
        then
            curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o installer.sh
            ./installer.sh -b -p ./miniconda3_tmp
            conda init zsh
        fi
        conda create -n ${env_name} --file https://ssb.stsci.edu/releases/jwstdp/${PIPELINE_VERSION}/conda_python_macos-stable-deps.txt
        conda activate ${env_name}
        pip install -r https://ssb.stsci.edu/releases/jwstdp/${PIPELINE_VERSION}/reqs_macos-stable-deps.txt
    ;;
    Linux)
        if ! command -v conda &> /dev/null
        then
            curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o installer.sh
            ./installer.sh -b -p ./miniconda3_tmp
            conda init zsh
        fi
        conda create -n ${env_name} --file https://ssb.stsci.edu/releases/jwstdp/${PIPELINE_VERSION}/conda_python_stable-deps.txt
        conda activate ${env_name}
        pip install -r https://ssb.stsci.edu/releases/jwstdp/${PIPELINE_VERSION}/reqs_stable-deps.txt
    ;;
esac

conda env update --name ${env_name} --file notebook_supplement.yml --prune
