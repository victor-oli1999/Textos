function Botoes() {
    return (
      <div className="Botoes">
        <div className="radio">
            <input type="radio" id="bom-dia" name="saudacao" value="bom-dia"/>
            <label for="bom-dia">Bom dia!</label>
            
            <input type="radio" id="boa-tarde" name="saudacao" value="boa-tarde"/>
            <label for="boa-tarde">Boa tarde!</label>

            <input type="radio" id="sem" name="saudacao" value="sem"/>
            <label for="sem">Sem saudação</label>
        </div>
        <div className="cliente--nome">
            <input type="text" id="nome-cliente" placeholder="Nome do cliente" />
        </div>
        <div className="check--box">
            <input type="checkbox" id="introducao" name="introducao" />
            <label>Me introduzir</label>
            <input type="checkbox" id="assinatura" name="assinatura" />
            <label>Assinatura</label>
        </div>
      </div>
    );
  }
  
  export default Botoes;
  