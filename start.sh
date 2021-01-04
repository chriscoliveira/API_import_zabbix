


ip=$(hostname -I)

# Verifica se o input informado e valido como endereco IP
if ! echo "$ip" | grep -q '\([0-9]\{1,3\}\.\)\{3\}[0-9]\{1,3\}'; then
        echo 'Formato invalido para endereco IP'
        exit 1
fi

OLD_IFS=$IFS
IFS='.'

set - $ip

primeiro_octeto=$1
segundo_octeto=$2



IFS=$OLD_IFS


CT=$segundo_octeto

#
# corrige o ip da loja

if [ $CT -eq "88" ] 
then
    CTC="08"
else
    if [ $CT -eq "102" ] 
    then
        CTC="47"
    else
        if [ $CT -eq "103" ] 
        then
            CTC="48"
        else
            if [ $CT -eq "104" ] 
            then
                CTC="49"
            else
                if [ $CT -eq "105" ] 
                then
                    CTC="50"
                else
                    if [ $CT -eq "106" ] 
                    then
                        CTC="51"
                    else
                        CTC=$CT
                    fi
                fi
            fi
        fi
    fi

fi
if [ $CT -lt 10 ]
then
	CTC="0$CT"
fi

echo $CTC

echo "Digite 1 - Cadastrar novos Hosts\nDigite 2 - Criar Mapa (apenas se ja tiver cadastrado os hosts)"
read opcao
case $opcao in 
1) python3 API-ZABBIX.py $CTC ;;
2) python api_cria_mapa.py $CTC ;;
*) exit ;;
esac
