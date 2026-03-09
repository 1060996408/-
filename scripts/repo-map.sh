#!/bin/bash
# 代码库地图生成器
# 用途: 快速了解代码库结构

set -e

# 颜色定义
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== 📁 目录结构 ===${NC}"
echo ""
tree -L 3 -I 'node_modules|.git|dist|build|__pycache__|.next|.venv|venv' --dirsfirst 2>/dev/null || {
    echo "tree 命令未安装,使用 find 替代:"
    find . -maxdepth 3 -type d \
        -not -path "*/node_modules/*" \
        -not -path "*/.git/*" \
        -not -path "*/dist/*" \
        -not -path "*/build/*" \
        | sort
}

echo ""
echo -e "${BLUE}=== 📄 主要文件 (前 50 个) ===${NC}"
echo ""
find . -type f \( \
    -name "*.js" -o \
    -name "*.ts" -o \
    -name "*.jsx" -o \
    -name "*.tsx" -o \
    -name "*.py" -o \
    -name "*.go" -o \
    -name "*.java" -o \
    -name "*.rs" \
\) \
    -not -path "*/node_modules/*" \
    -not -path "*/.git/*" \
    -not -path "*/dist/*" \
    -not -path "*/build/*" \
    -not -path "*/__pycache__/*" \
    | sort \
    | head -50

echo ""
echo -e "${YELLOW}=== 🔧 关键函数/类 (前 30 个) ===${NC}"
echo ""
grep -rn "^function\|^class\|^def \|^export function\|^export class" \
    --include="*.js" \
    --include="*.ts" \
    --include="*.jsx" \
    --include="*.tsx" \
    --include="*.py" \
    --exclude-dir=node_modules \
    --exclude-dir=.git \
    --exclude-dir=dist \
    --exclude-dir=build \
    --exclude-dir=__pycache__ \
    2>/dev/null \
    | head -30 \
    || echo "未找到函数/类定义"

echo ""
echo -e "${GREEN}=== 📊 统计信息 ===${NC}"
echo ""

# 统计文件数量
total_files=$(find . -type f \
    -not -path "*/node_modules/*" \
    -not -path "*/.git/*" \
    -not -path "*/dist/*" \
    -not -path "*/build/*" \
    | wc -l)

code_files=$(find . -type f \( \
    -name "*.js" -o -name "*.ts" -o -name "*.py" -o \
    -name "*.jsx" -o -name "*.tsx" -o -name "*.go" \
\) \
    -not -path "*/node_modules/*" \
    -not -path "*/.git/*" \
    | wc -l)

echo "总文件数: $total_files"
echo "代码文件数: $code_files"

# 统计代码行数
if command -v cloc &> /dev/null; then
    echo ""
    echo "代码行数统计:"
    cloc . --exclude-dir=node_modules,.git,dist,build --quiet
else
    total_lines=$(find . -type f \( \
        -name "*.js" -o -name "*.ts" -o -name "*.py" \
    \) \
        -not -path "*/node_modules/*" \
        -not -path "*/.git/*" \
        -exec wc -l {} + 2>/dev/null \
        | tail -1 \
        | awk '{print $1}')
    echo "代码总行数 (估算): $total_lines"
fi

echo ""
echo -e "${GREEN}✅ 代码库地图生成完成${NC}"
