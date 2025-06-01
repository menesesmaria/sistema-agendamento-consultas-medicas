-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 01/06/2025 às 21:00
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `sistema_agendamento`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `consulta`
--

CREATE TABLE `consulta` (
  `id` int(11) NOT NULL,
  `paciente_id` int(11) DEFAULT NULL,
  `profissional_id` int(11) DEFAULT NULL,
  `especialidade_id` int(11) DEFAULT NULL,
  `disponibilidade_id` int(11) DEFAULT NULL,
  `situacao` varchar(50) NOT NULL,
  `pagamento` varchar(50) NOT NULL,
  `plano_saude_id` int(11) DEFAULT NULL,
  `descricao` text NOT NULL,
  `prescricao` text NOT NULL,
  `diagnostico` text NOT NULL,
  `exames_solicitados` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `disponibilidade`
--

CREATE TABLE `disponibilidade` (
  `id` int(11) NOT NULL,
  `profissional_id` int(11) NOT NULL,
  `data_horario` datetime NOT NULL,
  `duracao_consulta` int(11) NOT NULL,
  `disponivel` tinyint(1) NOT NULL DEFAULT 1,
  `bloqueado` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `especialidade`
--

CREATE TABLE `especialidade` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `descricao` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `paciente`
--

CREATE TABLE `paciente` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `telefone` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `cpf` varchar(14) NOT NULL,
  `data_nascimento` date NOT NULL,
  `obs_medicas` text DEFAULT NULL,
  `bairro` varchar(30) NOT NULL,
  `rua` varchar(30) NOT NULL,
  `numero_residencia` int(11) NOT NULL,
  `cep` varchar(8) NOT NULL,
  `sexo` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `paciente_plano`
--

CREATE TABLE `paciente_plano` (
  `id` int(11) NOT NULL,
  `paciente_id` int(11) NOT NULL,
  `plano_id` int(11) NOT NULL,
  `validade` date NOT NULL,
  `numero_registro` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `plano_saude`
--

CREATE TABLE `plano_saude` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `profissional`
--

CREATE TABLE `profissional` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `sexo` varchar(5) NOT NULL,
  `data_nascimento` date NOT NULL,
  `telefone` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `tempo_experiencia` varchar(15) NOT NULL,
  `nivel` varchar(50) NOT NULL,
  `instituicao_formacao` varchar(100) NOT NULL,
  `especialidade_medica_id` int(11) DEFAULT NULL,
  `bairro` varchar(30) NOT NULL,
  `rua` varchar(30) NOT NULL,
  `numero_residencia` int(11) NOT NULL,
  `cep` varchar(8) NOT NULL,
  `cpf` varchar(20) NOT NULL,
  `crm` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `profissional_plano`
--

CREATE TABLE `profissional_plano` (
  `id` int(11) NOT NULL,
  `profissional_id` int(11) NOT NULL,
  `plano_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `consulta`
--
ALTER TABLE `consulta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `paciente_id` (`paciente_id`),
  ADD KEY `profissional_id` (`profissional_id`),
  ADD KEY `especialidade_id` (`especialidade_id`),
  ADD KEY `disponibilidade_id` (`disponibilidade_id`),
  ADD KEY `plano_saude_id` (`plano_saude_id`);

--
-- Índices de tabela `disponibilidade`
--
ALTER TABLE `disponibilidade`
  ADD PRIMARY KEY (`id`),
  ADD KEY `profissional_id` (`profissional_id`);

--
-- Índices de tabela `especialidade`
--
ALTER TABLE `especialidade`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `paciente_plano`
--
ALTER TABLE `paciente_plano`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `paciente_id` (`paciente_id`,`plano_id`),
  ADD KEY `plano_id` (`plano_id`);

--
-- Índices de tabela `plano_saude`
--
ALTER TABLE `plano_saude`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `profissional`
--
ALTER TABLE `profissional`
  ADD PRIMARY KEY (`id`),
  ADD KEY `especialidade_medica_id` (`especialidade_medica_id`);

--
-- Índices de tabela `profissional_plano`
--
ALTER TABLE `profissional_plano`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `profissional_id` (`profissional_id`,`plano_id`),
  ADD KEY `plano_id` (`plano_id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `consulta`
--
ALTER TABLE `consulta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `disponibilidade`
--
ALTER TABLE `disponibilidade`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `especialidade`
--
ALTER TABLE `especialidade`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `paciente`
--
ALTER TABLE `paciente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `paciente_plano`
--
ALTER TABLE `paciente_plano`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `plano_saude`
--
ALTER TABLE `plano_saude`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `profissional`
--
ALTER TABLE `profissional`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `profissional_plano`
--
ALTER TABLE `profissional_plano`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `consulta`
--
ALTER TABLE `consulta`
  ADD CONSTRAINT `consulta_ibfk_1` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `consulta_ibfk_2` FOREIGN KEY (`profissional_id`) REFERENCES `profissional` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `consulta_ibfk_3` FOREIGN KEY (`especialidade_id`) REFERENCES `especialidade` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `consulta_ibfk_4` FOREIGN KEY (`disponibilidade_id`) REFERENCES `disponibilidade` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `consulta_ibfk_5` FOREIGN KEY (`plano_saude_id`) REFERENCES `plano_saude` (`id`) ON DELETE SET NULL;

--
-- Restrições para tabelas `disponibilidade`
--
ALTER TABLE `disponibilidade`
  ADD CONSTRAINT `disponibilidade_ibfk_1` FOREIGN KEY (`profissional_id`) REFERENCES `profissional` (`id`) ON DELETE CASCADE;

--
-- Restrições para tabelas `paciente_plano`
--
ALTER TABLE `paciente_plano`
  ADD CONSTRAINT `paciente_plano_ibfk_1` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `paciente_plano_ibfk_2` FOREIGN KEY (`plano_id`) REFERENCES `plano_saude` (`id`) ON DELETE CASCADE;

--
-- Restrições para tabelas `profissional`
--
ALTER TABLE `profissional`
  ADD CONSTRAINT `profissional_ibfk_1` FOREIGN KEY (`especialidade_medica_id`) REFERENCES `especialidade` (`id`) ON DELETE SET NULL;

--
-- Restrições para tabelas `profissional_plano`
--
ALTER TABLE `profissional_plano`
  ADD CONSTRAINT `profissional_plano_ibfk_1` FOREIGN KEY (`profissional_id`) REFERENCES `profissional` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `profissional_plano_ibfk_2` FOREIGN KEY (`plano_id`) REFERENCES `plano_saude` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
